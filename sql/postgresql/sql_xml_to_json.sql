select carrier_trading_partner_id,
       carrier_scac,
       carrier_quote_id,
       shipment_tender_id,
       purpose,
       po_num,
       order_num,
       bol_num,
       equipment_type,
       payment_terms,
       respond_by_date || ' ' || respond_by_time                                                   respond_by,
       time_zone,
       total_charge,
       cargo_value::decimal(12, 4), currency_code,
       insurance_amount::decimal(12, 4), mileage::float, (select json_build_object('company',
                                                                                   json_build_object('name', name, 'id', company_id),
                                                                                   'address', json_build_object(
                                                                                           'address', address,
                                                                                           'city', city,
                                                                                           'state', state,
                                                                                           'zip', zip,
                                                                                           'country', country
                                                                                       ),
                                                                                   'contact', json_build_object(
                                                                                           'name', contact_name,
                                                                                           'phone', contact_phone,
                                                                                           'fax', contact_fax
                                                                                       ))
                                                          from edi_test, XMLTABLE(
                                                                  '/sendLoadTenderRequest/loadTender/billTo'
                                                                      passing
                                edi_xml
                                COLUMNS
                                    name text PATH './companyName/text()',
                                                                  company_id text PATH './companyId/text()',
                                                                  "address" text PATH './addr/text()',
                                                                  "city" text PATH './city/text()',
                                                                  "state" text PATH './state/text()',
                                                                  "zip" text PATH './zip/text()',
                                                                  "country" text PATH './country/text()',
                                                                  "contact_name" text PATH './contact/contactName/text()',
                                                                  "contact_phone" text PATH './contact/phone/text()',
                                                                  "contact_fax" text PATH './contact/fax/text()',
                                                                  "contact_email" text PATH './contact/email/text()'
                                                              )) bill_to,

       to_json(array(select json_build_object('number', stop_num,
                                       'type', stop_type,
                                       'instructions', stop_instructions,
                                       'appointment_required', appointment_required::bool,
                                       'expected_date', expected_date || ' ' || expected_time_start,
                                       'time_zone', time_zone,
                                       'company', json_build_object('name', company_name,
                                                                    'id', company_id),
                                       'contacts', to_json(array((select json_build_object(
                                                                                 'name',
                                                                                 unnest(xpath('.//contactName/text()', p)),
                                                                                 'phone',
                                                                                 unnest(xpath('.//phone/text()', p)),
                                                                                 'fax',
                                                                                 unnest(xpath('.//fax/text()', p)),
                                                                                 'email',
                                                                                 unnest(xpath('.//email/text()', p))
                                                                             )
                                                                  from xml(contacts) p))),
                                       'accessorials', to_json(array((select json_build_object(
                                                                                     'name',
                                                                                     unnest(xpath('.//name/text()', p)),
                                                                                     'code', '',
                                                                                     'charge', 0
                                                                                 )
                                                                      from xml(accessorials) p))),
                                       'reference_numbers', to_json(array((select json_build_object(
                                                                                          'type',
                                                                                          unnest(xpath('.//type/text()', p)),
                                                                                          'text',
                                                                                          unnest(xpath('.//text/text()', p)),
                                                                                          'value',
                                                                                          unnest(xpath('.//value/text()', p))
                                                                                      )
                                                                           from xml(reference_nums) p)))
                         ) stop
              from edi_test, XMLTABLE('/sendLoadTenderRequest/loadTender/stops/*'
                                                               passing
                                      edi_xml
                                      COLUMNS stop_num text PATH './stopNum/text()',
                                      "stop_type" text PATH './stopType/text()',
                                      "stop_instructions" text PATH './stopInstructions/text()',
                                      "appointment_required" text PATH './apptRequired/text()',
                                      "expected_date" text PATH './expectedDate/text()',
                                      "expected_time_start" text PATH './expectedTimeStart/text()',
                                      "time_zone" text PATH './timeZone/text()',
                                      "company_name" text PATH './company/companyName/text()',
                                      "company_id" text PATH './company/companyId/text()',
                                      "contacts" xml PATH './contacts',
                                      "reference_nums" xml PATH './referenceNums',
                                      "accessorials" xml PATH './accessorials'
           )))                                                                                     stops,


       to_json(array(select json_build_object('type', type, 'text', text, 'value', value) reference_number
              from edi_test, XMLTABLE('/sendLoadTenderRequest/loadTender/referenceNums/*'
                                                               passing
                                      edi_xml
                                      COLUMNS type text PATH './type/text()',
                                      "text" text PATH './text/text()',
                                      "value" text PATH './value/text()'
           )))                                                                                     reference_numbers,

       to_json(array(select json_build_object('type', type, 'description', "desc", 'amount', amount::decimal(12, 4)) charge
              from edi_test, XMLTABLE('/sendLoadTenderRequest/loadTender/charges/*'
                                                               passing
                                      edi_xml
                                      COLUMNS type text PATH './type/text()',
                                      "desc" text PATH './desc/text()',
                                      "amount" text PATH './amount/text()'
           )))                                                                                     charges,
       to_json(array(select json_build_object('pickup_stop_number', pickup_stop_num::integer,
    'drop_off_stop_number', "dropoffStopNum"::integer,
    'item_number', "itemNum",
    'description', "desc",
    'handling_unit_count', "handlingUnitCount"::integer,
    'handling_units', "handlingUnits",
    'packaging_unit_count', "packagingUnitCount"::integer,
    'packaging_units', "packagingUnits",
    'weight', "weight"::float,
    'weight_units', "weightUnits",
    'length', "length"::float,
    'width', "width"::float,
    'height', "height"::float,
    'dimension_units', "dimensionUnits",
    'volume', "volume"::float,
    'volume_units', "volumeUnits",
    'nmfc_class', "nmfcClass",
    'nmfc_number', "nmfcNum",
    'is_hazardous', "isHazardousMaterials"::bool

    ) item
              from edi_test, XMLTABLE('/sendLoadTenderRequest/loadTender/items/*'
                                                               passing
                                      edi_xml
                                      COLUMNS
                                          pickup_stop_num text PATH './pickupStopNum/text()',
                                      "dropoffStopNum" text PATH './dropoffStopNum/text()',
                                      "itemNum" text PATH './itemNum/text()',
                                      "desc" text PATH './desc/text()',
                                      "handlingUnitCount" text PATH './handlingUnitCount/text()',
                                      "handlingUnits" text PATH './handlingUnits/text()',
                                      "packagingUnitCount" text PATH './packagingUnitCount/text()',
                                      "packagingUnits" text PATH './packagingUnits/text()',
                                      "weight" text PATH './weight/text()',
                                      "weightUnits" text PATH './weightUnits/text()',
                                      "length" text PATH './length/text()',
                                      "width" text PATH './weight/text()',
                                      "height" text PATH './height/text()',
                                      "dimensionUnits" text PATH './dimensionUnits/text()',
                                      "volume" text PATH './volume/text()',
                                      "volumeUnits" text PATH './volumeUnits/text()',
                                      "nmfcClass" text PATH './nmfcClass/text()',
                                      "nmfcNum" text PATH './nmfcNum/text()',
                                      "isHazardousMaterials" text PATH './isHazardousMaterials/text()'
           )))                                                                                     items,
       to_json(array(select json_build_object('special_instruction', special_instruction)
              from edi_test, XMLTABLE('/sendLoadTenderRequest/loadTender/specialInstructions/specialInstruction'
           passing
                                      edi_xml
                                      COLUMNS special_instruction text PATH 'text()'))) special_instructions

from tender_transaction, XMLTABLE('/sendLoadTenderRequest/loadTender/shipmentId' passing transaction_payload_xml
                        COLUMNS
                            carrier_trading_partner_id text PATH '../carrierTradingPartnerId/text()',
                        carrier_scac text PATH '../carrierSCAC/text()',
                        carrier_quote_id text PATH '../carrierQuoteId/text()',
                        shipment_tender_id text PATH 'text()',
                        purpose text PATH '../purpose/text()',
                        po_num text PATH '../poNum/text()',
                        pro_num text PATH '../proNum/text()',
                        order_num text PATH '../orderNum/text()',
                        bol_num text PATH '../bolNum/text()',
                        mode text PATH '../mode/text()',
                        equipment_type text PATH '../equipmentType/text()',
                        respond_by_date text PATH '../respondByDate/text()',
                        respond_by_time text PATH '../respondByTime/text()',
                        time_zone text PATH '../timeZone/text()',
                        total_charge text PATH '../totalCharge/text()',
                        cargo_value text PATH '../cargoValue/text()',
                        insurance_amount text PATH '../insuranceAmount/text()',
                        currency_code text PATH '../currencyCode/text()',
                        mileage text PATH '../mileage/text()',
                        payment_terms text PATH '../paymentTerms/text()'
    )
where transaction_payload_xml is not null and transaction_type = '204' and direction = 'outbound';