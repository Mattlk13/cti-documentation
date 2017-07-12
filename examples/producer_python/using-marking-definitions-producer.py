import stix2

identity = stix2.Identity(
    id="identity--611d9d41-dba5-4e13-9b29-e22488058ffc",
    created="2017-04-14T13:07:49.812Z",
    modified="2017-04-14T13:07:49.812Z",
    name="Stark Industries",
    contact_information="info@stark.com",
    identity_class="organisation",
    sectors=["defence"]
)

marking_def_amber = stix2.MarkingDefinition(
    id="marking-definition--f88d31f6-486f-44da-b317-01333bde0b82",
    created="2017-01-20T00:00:00.000Z",
    definition_type="tlp",
    definition={
        "tlp": "amber"
    }
)

marking_def_statement = stix2.MarkingDefinition(
    id="marking-definition--d81f86b9-975b-bc0b-775e-810c5ad45a4f",
    created="2017-04-14T13:07:49.812Z",
    definition_type="statement",
    definition=stix2.StatementMarking("Copyright (c) Stark Industries 2017.")
)

indicator = stix2.Indicator(
    id="indicator--33fe3b22-0201-47cf-85d0-97c02164528d",
    created="2017-04-14T13:07:49.812Z",
    modified="2017-04-14T13:07:49.812Z",
    created_by_ref="identity--611d9d41-dba5-4e13-9b29-e22488058ffc",
    name="Known malicious IP Address",
    labels=["malicious-activity"],
    pattern="[ipv4-addr:value = '10.0.0.0']",
    valid_from="2017-04-14T13:07:49.812Z",
    object_marking_refs=[marking_def_amber, marking_def_statement]
)

bundle = stix2.Bundle(objects=[identity, indicator, marking_def_amber, marking_def_statement])
