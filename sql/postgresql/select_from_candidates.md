Case study: Contract Routes

We have contracts and routes, these are associated via a table called contract_route. Each contract can be associated with multiple routes, and routes can be marked as primary true or false. At any point in time there must only be one single primary route per contract and the contract must always have a primary route.

+------------------------------------+------------------------------------+---------------------------------+----------+
|contract_id                         |route_id                            |created_at                       |is_primary|
+------------------------------------+------------------------------------+---------------------------------+----------+
|6d871c6b-6e9f-11ed-9792-b1386f99ee7a|2e383c02-4893-420a-820d-b9a085484261|2022-11-27 22:05:22.178152 +00:00|false     |
|6d871c6b-6e9f-11ed-9792-b1386f99ee7a|4c2a9cb6-fa27-4d99-9f3b-8cd92013eb65|2022-11-27 22:04:32.108696 +00:00|false     |
|6d871c6b-6e9f-11ed-9792-b1386f99ee7a|18b42de4-3952-4a32-b207-7a44c1a93c6a|2022-11-27 22:04:17.850949 +00:00|true      |
|991c63af-c35f-40c6-a059-74e7385207c2|64b7d4be-2f05-4b37-b957-c9a4284f8be3|2022-11-27 22:02:03.810804 +00:00|true      |
|bb23948c-6e9f-11ed-9792-e5cdb7befbb3|4c2a9cb6-fa27-4d99-9f3b-8cd92013eb65|2022-11-27 22:06:46.943060 +00:00|false     |
|bb23948c-6e9f-11ed-9792-e5cdb7befbb3|18b42de4-3952-4a32-b207-7a44c1a93c6a|2022-11-27 22:06:30.566146 +00:00|true      |
+------------------------------------+------------------------------------+---------------------------------+----------+

Selecting only a single route per contract

select distinct on (contract_id) contract_id, route_id
from contracting.contract_route crt
where is_primary
order by  contract_id, created_at desc;

An efficient and easy to read way to solve this is to use the distinct on expression in Postgres.

With DISTINCT ON, you tell PostgreSQL to return a single row for each distinct group defined by the ON clause. Which row in that group is returned is specified with the ORDER BY clause.

We’re telling Postgres to “put the rows into groups unique by url (ON (contract_id)), sort each of these groups by most recent (ORDER BY contract_id, created_at DESC) and then return fields for the first record in each of these groups (contract_id, route_id).

For more reading see: https://www.geekytidbits.com/postgres-distinct-on/

The result is:

+------------------------------------+------------------------------------+
|contract_id                         |route_id                            |
+------------------------------------+------------------------------------+
|6d871c6b-6e9f-11ed-9792-b1386f99ee7a|18b42de4-3952-4a32-b207-7a44c1a93c6a|
|991c63af-c35f-40c6-a059-74e7385207c2|64b7d4be-2f05-4b37-b957-c9a4284f8be3|
|bb23948c-6e9f-11ed-9792-e5cdb7befbb3|18b42de4-3952-4a32-b207-7a44c1a93c6a|
+------------------------------------+------------------------------------+

Ensuring that there is always a primary route and only one primary route

Here what we want to do is:

    select the contracts that have a primary route and only one of their primary routes as P={ (contract, route) | route is primary, unique on contract }

    select the contracts that are not in the primary routes N ={contracts | contract not in P} these are the contracts without any primary routes associated

    Set all routes to non primary that are not in P.

    Set all routes to primary that are in N.

with primary_routes as (
    -- select all contracts and their primary routes distinct will eliminate duplicate primary route ids
    select distinct on (contract_id) contract_id, route_id
    from contracting.contract_route crt
    where is_primary
    order by contract_id, route_id, created_at desc
),
     should_be_primary as (
         -- select all contracts that do not have a route id with is primary and select any route id but only one
         select distinct on (contract_id) contract_id, route_id
         from contracting.contract_route
         where contract_id not in (select contract_id from primary_routes)
         order by contract_id, route_id, created_at desc
     ),
     update_non_primaries as (
         -- every contract routeid that is not in primary_routes is set to false
         update contracting.contract_route cr
             set is_primary = false
             where not exists(select 1
                              from primary_routes pr2
                              where pr2.contract_id = cr.contract_id and pr2.route_id = cr.route_id)
     )
     -- every contract route id in should_be_primary is set to true
update contracting.contract_route cr
set is_primary= true
where exists(select 1 from should_be_primary pr2 
where pr2.contract_id = cr.contract_id and pr2.route_id = cr.route_id)
                