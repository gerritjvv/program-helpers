-- use json_array_elements to build an array of objects which you can then use
-- as a table
with driver_budget_values as (
    select json_array_elements(json_build_array(
            json_build_object('id', 2, 'name', 'abc'),
            json_build_object('id', 4, 'name', 'edf')
        )) record
)
select * from driver_budget_values;