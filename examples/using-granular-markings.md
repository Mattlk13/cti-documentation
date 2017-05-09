---
layout: page
title: Using Granular Markings
categories: examples
---

Having finer, more granular restrictions over what cyber threat intelligence is shared is beneficial for organizations who are hesitant to sharing certain information. This element of control allows STIX producers to limit the accessibility of specific data to organizations with which they share intelligence.

**Scenario**
------------

This scenario focuses on a STIX producer, “Gotham National Bank”, who imposes granular markings on an Indicator object. Before sharing this indicator, Gotham selects a few “Traffic Light Protocol” (TLP) marking definitions to apply to the indicator. These marking definitions help restrict the usage of certain properties of the indicator based on its TLP marking type.

**Data model**
--------------

The producer of STIX objects in this scenario, Gotham National Bank, can be represented with an [Identity](https://docs.google.com/document/d/1S5XhY6F5OT599b0OuHtUf8IBzFvNY8RysFHIj93DgsY/edit#heading=h.wh296fiwpklp) STIX Domain Object (SDO). Like with all STIX objects, an <span class="sdo">**id**</span> attribute uniquely identifies Gotham National and can be referenced within all the objects they generate with the <span class="sdo">**created\_by\_ref**</span> property. Although <span class="sdo">**created\_by\_ref**</span> is optional, this is helpful for attributing the Indicator SDO directly to Gotham and allows any consumers to see who applied the TLP markings to the Indicator. The Identity object is also useful for listing other relevant details about Gotham such as <span class="sdo">**contact\_information**</span> and what type of identity they are with the <span class="sdo">**identity\_class**</span> field.

In order to enforce limitations on specific properties of the Indicator object, Gotham decided to use TLP Marking Definition objects. This particular marking definition type, which can be seen within the STIX 2.0 specification under [TLP Marking Object Type](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.yd3ar14ekwrs), helps specify the type of restriction they want to impose. For instance, in this scenario, they needed to utilize three defined TLP marking definitions, each with a different restriction type. With all of these objects, the <span class="sdo">**definition\_type**</span> is required and must be <span class="values">tlp</span>. In addition, the <span class="sdo">**definition**</span> property is also required and must contain one of the four types of TLP. Gotham needed three of the four types of TLP definitions, which were <span class="values">green</span>, <span class="values">amber</span>, and <span class="values">red</span>. To read about each of the four types of TLP and what restrictions they specify, check out [US-CERT’s TLP Definitions and Usage](https://www.us-cert.gov/tlp). Knowing these types is useful for the level of restriction you would like to provide for both objects and properties of objects.

A point of emphasis worth noting is that the TLP Marking Object Types defined in the STIX 2.0 specification must be used to represent TLP markings. Gotham or any other producer could not create their own TLP markings but could create organization-specific [Statement Marking Object Types](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.3ru8r05saera). Both of these types, TLP and Statement, also cannot be versioned like other STIX objects, which is why there is no <span class="sdo">**modified**</span> property on either of these types. To understand more about versioning objects, check out this helpful tutorial video on [How to Use Versioning in STIX 2](https://www.youtube.com/watch?v=s4c4PHUfttE).

Now that Gotham has selected the appropriate TLP Marking Object types, they can be applied to other STIX objects or properties of objects. In this scenario, they are attached to properties of an [Indicator](https://docs.google.com/document/d/1S5XhY6F5OT599b0OuHtUf8IBzFvNY8RysFHIj93DgsY/edit#heading=h.muftrcpnf89v) SDO Gotham generated. This Indicator was created to represent a fake email address suspected in emailing the bank's members asking for their credentials. Due to the sensitivity of some of the information contained within this Indicator, they applied different TLP markings to individual portions of this object with the <span class="sdo">**granular\_markings**</span> property. This property is a list that contains Marking Definition object ID references with the <span class="sdo">**marking\_ref**</span> field, and a <span class="sdo">**selectors**</span> property that specifies the content that should be marked with this marking definition. For instance, Gotham felt the need to apply strict TLP: Red markings to the <span class="sdo">**pattern**</span> and <span class="sdo">**description**</span> fields since they contain the most detailed and sensitive intelligence about the Indicator. To illustrate further, within the <span class="sdo">**granular\_markings**</span> field of the Indicator, the <span class="sdo">**marking\_ref**</span> property would contain the marking definition UUID for TLP: Red and the <span class="sdo">**selectors**</span> list would hold the values <span class="values">pattern</span> and <span class="values">description</span>.

For other Indicator properties, Gotham used less restrictive TLP markings than TLP: Red. One required Indicator property is a list of <span class="sdo">**labels**</span>, which gives more context about the type of indicator being modeled. In this property list, Gotham labeled this indicator as both <span class="values">malicious-activity</span> and <span class="values">fake-email</span>. The first label in the list, <span class="values">malicious-activity</span>, comes from the [Indicator Label Open Vocabulary](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.cvhfwe3t9vuo) and the 2nd label, <span class="values">fake-email</span>, is one Gotham chose since they are free to apply their own labels outside of the recommended STIX 2.0 vocabulary. Since <span class="values">malicious-activity</span> is a more generic label than <span class="values">fake-email</span>, Gotham applied the less restrictive TLP: Green marking. However for <span class="values">fake-email</span>, Gotham felt the need to attach a more moderately restrictive marking of TLP: Amber. In order to communicate two different markings like this on the <span class="sdo">**labels**</span> property, you would represent the first label in the list as <span class="values">labels\[0\]</span>, and the second as <span class="values">labels\[1\]</span>. To illustrate this, the JSON sample below shows how these would be marked if we were just marking the <span class="sdo">**labels**</span> field only (Note: Marking Definition ID starting with "f88..." is TLP: Amber and the ID starting with "340..." is TLP: Green):

```
{
"granular_markings": [  
  {
    "marking_ref": "marking-definition--f88d31f6-486f-44da-b317-01333bde0b82",
    "selectors": [    
      "labels.[1]"
    ]
  },
  {
    "marking_ref": "marking-definition--34098fce-860f-48ae-8e50-ebd3cc5e41da",
    "selectors": [
      "labels.[0]",      
    ]
  }
]}
```

Along with these Indicator <span class="sdo">**labels**</span>, Gotham chose to mark the property <span class="sdo">**name**</span> as TLP: Amber and the property <span class="sdo">**valid\_from**</span> as TLP: Green. They can mark any property they would like but cannot mark invalid properties such as <span class="values">labels\[3\]</span>, or <span class="values">kill\_chain\_phases\[0\]</span> since these are not present currently within this Indicator SDO.

The full JSON representation can be seen at the very end of this example and a diagram of the scenario is illustrated below:

![Using Granular Markings Diagram]({{ site.baseurl }}/img/Using-granular-markings.PNG)

**Further Reading**
-------------------

To read more about the objects in this example as well as common properties and vocabularies, check out the links below:

-   [Common Properties](https://docs.google.com/document/d/1HRVFn2kAxBOTMbEb3KRu8tjMoHm-KRAI-2R8CTzGil4/edit#heading=h.xzbicbtscatx)
-   [Vocabularies](https://docs.google.com/document/d/1HRVFn2kAxBOTMbEb3KRu8tjMoHm-KRAI-2R8CTzGil4/edit#heading=h.iit7tolczlxv)
-   [Identity](https://docs.google.com/document/d/1nipwFIaFwkHo4Gzw-qxZQpCjP_5tX7rbI3Ic5C56Z88/edit#heading=h.wh296fiwpklp)
-   [Indicator](https://docs.google.com/document/d/1S5XhY6F5OT599b0OuHtUf8IBzFvNY8RysFHIj93DgsY/edit#heading=h.muftrcpnf89v)
-   [Marking Definitions](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.j0uqagkk6m9n)
-   [Granular Markings](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.robezi5egfdr)
-   [Statement Marking Object Type](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.3ru8r05saera)
-   [TLP Object Marking Type](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.yd3ar14ekwrs)
-   [STIX Patterning](https://docs.google.com/document/d/1suvd7z7YjNKWOwgko-vJ84jfGuxSYZjOQlw5leCswPY/edit)
-   [Using Versioning in STIX 2](https://www.youtube.com/watch?v=s4c4PHUfttE)

**JSON**
------------------

```
{
  "type": "bundle",
  "id": "bundle--963410f2-fd7d-4d80-937c-8ad3aed5f432",
  "spec_version": "2.0",
  "objects": [
    {
      "type": "identity",
      "id": "identity--b38dfe21-7477-40d1-aa90-5c8671ce51ca",
      "created": "2017-04-27T16:18:24.318Z",
      "modified": "2017-04-27T16:18:24.318Z",
      "name": "Gotham National Bank",
      "identity_class": "organization",
      "contact_information": "contact@gothamnational.com",
      "sectors": [
        "financial-services"
      ]
    },
    {
      "type": "marking-definition",
      "id": "marking-definition--34098fce-860f-48ae-8e50-ebd3cc5e41da",
      "created": "2017-01-20T00:00:00.000Z",
      "definition_type": "tlp",
      "definition": {
        "tlp": "green"
      }
    },
    {
      "type": "marking-definition",
      "id": "marking-definition--f88d31f6-486f-44da-b317-01333bde0b82",
      "created": "2017-01-20T00:00:00.000Z",
      "definition_type": "tlp",
      "definition": {
        "tlp": "amber"
      }
    },
    {
      "type": "marking-definition",
      "id": "marking-definition--5e57c739-391a-4eb3-b6be-7d15ca92d5ed",
      "created": "2017-01-20T00:00:00.000Z",
      "definition_type": "tlp",
      "definition": {
        "tlp": "red"
      }
    },
    {
      "type": "indicator",
      "id": "indicator--1ed8caa7-a708-4706-b651-f1186ede6ca1",
      "created": "2017-04-27T16:18:24.318Z",
      "modified": "2017-04-27T16:18:24.318Z",
      "created_by_ref": "identity--b38dfe21-7477-40d1-aa90-5c8671ce51ca",
      "name": "Fake email address",
      "description": "Messages from this false email address been sent to customers.",
      "labels": [
        "malicious-activity",
        "fake-email"
      ],
      "pattern": "[email-message:from_ref.value MATCHES '.+\\\\banking@g0thamnatl\\\\.com$']",
      "valid_from": "2017-04-27T16:18:24.318Z",
      "granular_markings": [
        {
          "marking_ref": "marking-definition--5e57c739-391a-4eb3-b6be-7d15ca92d5ed",
          "selectors": [
            "pattern",
            "description"
          ]
        },
        {
          "marking_ref": "marking-definition--f88d31f6-486f-44da-b317-01333bde0b82",
          "selectors": [
            "name",
            "labels.[1]"
          ]
        },
        {
          "marking_ref": "marking-definition--34098fce-860f-48ae-8e50-ebd3cc5e41da",
          "selectors": [
            "labels.[0]",
            "valid_from"
          ]
        }
      ]
    }
  ]
}

```
