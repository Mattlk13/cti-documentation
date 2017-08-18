---
layout: page
title: About
categories: stix
---

<div class="well info-box" markdown="span">Familiar with STIX 1.x?<br/> Here’s a [comparison to 2.0](compare).</div>

Structured Threat Information Expression (STIX™) is a language for describing cyber threat information in a standardized and structured manner to enable the exchange of cyber threat intelligence (CTI). STIX characterizes an extensive set of CTI to include indicators of adversary activity, as well as contextual information characterizing cyber adversary motivations, capabilities, and activities and best courses of action for defense and mitigation.

A set of [specifications](https://docs.google.com/document/d/1yvqWaPPnPW-2NiVCLqzRszcx91ffMowfT5MmE9Nsy_w/edit#heading=h.t32x0azc539r) provide the normative description of STIX 2.0. While STIX 2.0 is defined to be independent of any specific serialization, JSON is the mandatory-to-implement serialization and informative [JSON schemas](https://github.com/oasis-open/cti-stix2-json-schemas) are available. The following is a JSON-based example of a [STIX 2.0 Campaign object](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.pcpvfz4ik6d6):

```
{  
    "type": "campaign",  
    "id": "campaign--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",  
    "created": "2016-04-06T20:03:00.000Z",  
    "name": "Green Group Attacks Against Finance",  
    "description": "Campaign by Green Group against targets in the financial services sector."  
}
```

<div class="figure pull-right text-center" markdown="span">
![STIX 2.0 Relationship Example]({{ site.baseurl }}/img/stix2_relationship_example_2.png){: .figure-img .img-fluid}
**STIX 2.0 Relationship Example**
</div>

In addition to describing a set of STIX Domain Objects (SDOs), STIX 2.0 enables relationships to be defined *between* objects. As the example shows, a Campaign may be attributed to a Threat Actor and may target a Vulnerability while an Indicator indicates the Campaign.

A companion CTI specification, [TAXII](https://docs.google.com/document/d/1Jv9ICjUNZrOnwUXtenB1QcnBLO35RnjQcJLsa1mGSkI/pub)™, is designed specifically to transport STIX Objects. However, the structures and serializations of STIX do not rely on any specific transport mechanism, and STIX provides a “Bundle,” a container for STIX Objects to allow for transportation of bulk STIX data, especially over non-TAXII communication mechanisms.

Complete information for STIX 2.0 is available on the [OASIS Cyber Threat Intelligence (CTI) Technical Committee (TC)](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cti) website. [Specification documents](https://docs.google.com/document/d/1yvqWaPPnPW-2NiVCLqzRszcx91ffMowfT5MmE9Nsy_w/edit?pref=2&pli=1) and [schemas and tools](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cti#openrepo) are also available.

## STIX 2.0 Objects

STIX Objects represent a minimally viable product (MVP) that fulfills basic consumer and producer requirements for CTI sharing. Objects and properties not included in STIX 2.0, but deemed necessary by the community, will be included in future releases.

#### STIX 2.0 defines twelve STIX Domain Objects (SDOs):

{: .table .table-hover .table-example .table-desc}
| Object | Name | Description |
| :---: | :---: | --- |
| ![Attack Pattern Icon]({{ site.baseurl }}/img/icons/attack_pattern.png "Attack Pattern Icon") | [**Attack Pattern**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.axjijf603msy) | A type of Tactics, Techniques, and Procedures (TTP) that describes ways threat actors attempt to compromise targets. |
| ![Campaign Icon]({{ site.baseurl }}/img/icons/campaign.png "Campaign Icon") | [**Campaign**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.pcpvfz4ik6d6) | A grouping of adversarial behaviors that describes a set of malicious activities or attacks that occur over a period of time against a specific set of targets. |
| ![Course of Action Icon]({{ site.baseurl }}/img/icons/course_of_action.png "Course of Action Icon") | [**Course of Action**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.a925mpw39txn) | An action taken to either prevent an attack or respond to an attack. |
| ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png "Identity Icon") | [**Identity**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.wh296fiwpklp) | Individuals, organizations, or groups, as well as classes of individuals, organizations, or groups. 
| ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png "Indicator Icon") | [**Indicator**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.muftrcpnf89v) | Contains a pattern that can be used to detect suspicious or malicious cyber activity. |
| ![Intrusion Set Icon]({{ site.baseurl }}/img/icons/intrusion_set.png "Intrusion Set Icon") | [**Intrusion Set**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.5ol9xlbbnrdn) | A grouped set of adversarial behaviors and resources with common properties believed to be orchestrated by a single threat actor. |
| ![Malware Icon]({{ site.baseurl }}/img/icons/malware.png "Malware Icon") | [**Malware**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.s5l7katgbp09) | A type of TTP, also known as malicious code and malicious software, used to compromise the confidentiality, integrity, or availability of a victim’s data or system. |
| ![Observed Data Icon]({{ site.baseurl }}/img/icons/observed_data.png "Observed Data Icon") | [**Observed Data**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.p49j1fwoxldc) | Conveys information observed on a system or network (e.g., an IP address). |
| ![Report Icon]({{ site.baseurl }}/img/icons/report.png "Report Icon") | [**Report**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.n8bjzg1ysgdq) | Collections of threat intelligence focused on one or more topics, such as a description of a threat actor, malware, or attack technique, including contextual details. |
| ![Threat Actor Icon]({{ site.baseurl }}/img/icons/threat_actor.png "Threat Actor Icon") | [**Threat Actor**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.k017w16zutw) |Individuals, groups, or organizations believed to be operating with malicious intent. |
| ![Tool Icon]({{ site.baseurl }}/img/icons/tool.png "Tool Icon") | [**Tool**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.z4voa9ndw8v) | Legitimate software that can be used by threat actors to perform attacks. |
| ![Vulnerability Icon]({{ site.baseurl }}/img/icons/vulnerability.png "Vulnerability Icon") | [**Vulnerability**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.q5ytzmajn6re) | A mistake in software that can be directly used by a hacker to gain access to a system or network. |

#### STIX 2.0 defines two STIX Relationship Objects (SROs):

{:.table .table-hover .table-example .table-desc}
| Object | Name | Description |
| :---: | :---:| --- |
| ![Relationship Icon]({{ site.baseurl }}/img/icons/relationship.png "Relationship Icon") | [**Relationship**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.e2e1szrqfoan) | Used to link two SDOs and to describe how they are related to each other. |
| ![Sighting Icon]({{ site.baseurl }}/img/icons/sighting.png "Sighting Icon") | [**Sighting**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.a795guqsap3r) | Denotes the belief that an element of CTI was seen (e.g., indicator, malware). |

Objects Overview
----------------

The next video provides an overview of STIX 2.0 objects. It highlights the four types of objects in STIX 2: STIX Domain Objects (SDOs), STIX Relationship Objects (SROs), Marking Definition objects, and Bundle objects.

<div class="video-wrapper">
    <div class="video-container">
        <iframe src="https://www.youtube.com/embed/iAnd3rApMcA?ecver=2" width="640" height="360" frameborder="0"></iframe>
    </div>
    <!-- /video --><br><br>
</div>
<!-- /video-wrapper -->