---
layout: page
title: Examples and Tutorials
categories: stix
hide_title: true
---

STIX 2.0 Examples
=================

The examples below demonstrate how to use STIX 2.0 concepts for common use cases. They are useful for linking multiple concepts together and provide more detail regarding STIX objects and properties.


{:.table .table-hover .table-example .table-desc .table-anchor}

| Example | STIX Types | Description |
| --- | --- | --- |
| [Identifying a Threat Actor Profile](/cti-documentation/examples/identifying-a-threat-actor-profile) | ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png) ![Threat Actor Icon]({{ site.baseurl }}/img/icons/threat_actor.png) | Threat Actors often have several discernible characteristics such as aliases, goals and motivations which can be captured within a STIX Threat Actor object. In this example, the threat actor can also be attributed to an Identity object which models more basic identifiable information. |
| [Indicator for Malicious URL](/cti-documentation/examples/indicator-for-malicious-url)             | ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png) ![Malware Icon]({{ site.baseurl }}/img/icons/malware.png) | This example models a STIX Indicator object that represents a malicious URL using STIX patterning language. The Indicator indicates that it's a delivery mechanism for a piece of malware. |
| [Malware Indicator for File Hash](/cti-documentation/examples/malware-indicator-for-file-hash)         | ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png) ![Malware Icon]({{ site.baseurl }}/img/icons/malware.png) | File hashes for malware variants can be captured within an Indicator STIX Domain Object and then associated with a Malware object which provides more detail about the malware.  |
| [Sighting of an Indicator](/cti-documentation/examples/sighting-of-an-indicator) | ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png) ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png) ![Sighting Icon]({{ site.baseurl }}/img/icons/sighting.png) | Indicators on one organization's network are often spotted on other organizations' networks. When this is the case, a Sighting STIX Relationship Object (SRO) can be issued to relay that this specific indicator was seen. This example discusses how a company can use a Sighting for a STIX Indicator object.
| [Sighting of Observed-data](/cti-documentation/examples/sighting-of-observed-data) | ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png) ![Observed-data Icon]({{ site.baseurl }}/img/icons/observed_data.png) ![Sighting Icon]({{ site.baseurl }}/img/icons/sighting.png) ![Malware Icon]({{ site.baseurl }}/img/icons/malware.png) | Observed data represent machine-generated raw information and are different from Indicators which dictate more of an intelligence assertion. These Observed-data SDO's can still be shared and referenced within a Sighting SRO. This example demonstrates the usage of Observed-data and their relation to other STIX objects.
| [Threat Actor Leveraging Attack Patterns and Malware](/cti-documentation/examples/threat-actor-leveraging-attack-patterns-and-malware) | ![Attack Pattern Icon]({{ site.baseurl }}/img/icons/attack_pattern.png) ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png) ![Malware Icon]({{ site.baseurl }}/img/icons/malware.png) ![Threat Actor Icon]({{ site.baseurl }}/img/icons/threat_actor.png) | Threat actors can often be characterized by the attack patterns they leverage and the malware varieties they use. This example describes how to represent a threat actor who uses a phishing attack pattern to deliver a form of malware. |
| [Using Marking Definitions](/cti-documentation/examples/using-marking-definitions) | ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png) ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png) ![Amber Marking Icon]({{ site.baseurl }}/img/icons/tlp_amber.png) ![Statement Marking Icon]({{ site.baseurl }}/img/icons/restricted_marking.png) | Sometimes when creating STIX objects it may be useful to provide guidance or permissions on how those objects may be used. In this example, Marking Definition objects are created and applied to an Indicator object to specify restrictions and copyright information. |
| [Using Granular Markings](/cti-documentation/examples/using-granular-markings) | ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png) ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png) ![Green Marking Icon]({{ site.baseurl }}/img/icons/tlp_green.png) ![Amber Marking Icon]({{ site.baseurl }}/img/icons/tlp_amber.png) ![Red Marking Icon]({{ site.baseurl }}/img/icons/tlp_red.png) | Whereas object markings in STIX can limit or restrict how entire objects are used, granular markings delve deeper into the objects and focus on restricting specific individual properties. This example demonstrates how to enforce different TLP markings on multiple properties of an Indicator SDO. |
