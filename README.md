# Awesome SolidFire: An Unofficial Collection of NetApp SolidFire Resources

- [Awesome SolidFire: An Unofficial Collection of NetApp SolidFire Resources](#awesome-solidfire-an-unofficial-collection-of-netapp-solidfire-resources)
  - [NetApp SolidFire-based Offerings](#netapp-solidfire-based-offerings)
  - [Why SolidFire](#why-solidfire)
    - [Why NetApp HCI](#why-netapp-hci)
  - [Resources and Solutions](#resources-and-solutions)
    - [Cloud](#cloud)
    - [Virtualization](#virtualization)
      - [VMware vSphere](#vmware-vsphere)
      - [Microsoft Hyper-V](#microsoft-hyper-v)
      - [Linux-related (OpenStack, KVM, XenServer, Oracle VM)](#linux-related-openstack-kvm-xenserver-oracle-vm)
      - [Storage Provisioning for Containers (CSI and Docker)](#storage-provisioning-for-containers-csi-and-docker)
    - [CLI, API, SDK Resources](#cli-api-sdk-resources)
      - [CLI](#cli)
      - [SolidFire/Element Software Development Kits (SDKs)](#solidfireelement-software-development-kits-sdks)
    - [Automation](#automation)
      - [Automation and Configuration Tools and Frameworks](#automation-and-configuration-tools-and-frameworks)
    - [Alerting, Monitoring, Telemetry](#alerting-monitoring-telemetry)
      - [ActiveIQ](#activeiq)
      - [NetApp Cloud Insights](#netapp-cloud-insights)
      - [Grafana/Graphite - HCICollector](#grafanagraphite---hcicollector)
      - [Prometheus - solidfire-exporter](#prometheus---solidfire-exporter)
      - [Icinga and Nagios](#icinga-and-nagios)
      - [SNMP MIBs](#snmp-mibs)
      - [Syslog Forwarding](#syslog-forwarding)
      - [Event Notifications](#event-notifications)
    - [Backup, Restore, Site Failover](#backup-restore-site-failover)
  - [Demo VM, Tools and Utilities](#demo-vm-tools-and-utilities)
    - [SolidFire/Element Demo VM](#solidfireelement-demo-vm)
    - [Recorded Demos](#recorded-demos)
  - [Scripts and How-To Articles](#scripts-and-how-to-articles)
    - [VMware](#vmware)
    - [Windows](#windows)
  - [Questions and Answers](#questions-and-answers)
    - [Meta](#meta)
    - [Element Demo VM](#element-demo-vm)
    - [Hypervisors and Containers](#hypervisors-and-containers)
    - [Workloads](#workloads)
    - [Storage Services](#storage-services)
    - [DevOps](#devops)
    - [Networking](#networking)
  - [License and Trademarks](#license-and-trademarks)

## NetApp SolidFire-based Offerings

- SolidFire iSCSI storage clusters (available as storage-only clusters composed of storage nodes from NetApp HCI product line)
- NetApp HCI (NetApp HCI compute nodes connected via iSCSI to NetApp HCI storage nodes - some call it "disaggregated HCI" or dHCI)

## Why SolidFire

- Fully programmable storage - from the initial node configuration to automated storage provisioning for containers
- Cloud-like, set-and-forget iSCSI storage for clients ranging from bare metal x86_64 servers to hypervisors, VMs and containers
- Always-on effciency with zero-performance impact. Compression and deduplication cannot be disabled
- Granular storage capacity and performance management - Minimum, Maximum and Burst storage policies may be assigned on a per-volume basis
- General purpose scale-out storage clusters that are easy to provision, manage, refresh, and scale
- Can be merged into or serve as a base for NetApp HCI - add two or more NetApp HCI compute nodes and convert your SolidFire cluster into NetApp HCI

### Why NetApp HCI

- Open architecture
  - Connect 3rd party compute nodes to NetApp HCI storage (iSCSI). Get more out of your existing VMware, Linux, and Windows servers by connecting them to NetApp HCI storage over dedicated VLAN. For example you can attach your sandbox cluster to dedicated NetApp HCI iSCSI volumes and get all the benefits of SolidFire
  - Connect NetApp HCI compute nodes to NetApp or 3rd party storage (NFS or iSCSI). This way you can run very heavy workloads on NetApp HCI compute while offloading the heavy I/O to NetApp ONTAP or E-Series arrays
- Hybrid Cloud and Data Fabric integrations for a multi-cloud (including on-premises Private Cloud) world. Supports NetApp ONTAP Select, Cloud Volumes on HCI, and major Kubernetes platforms
- Easily and quickly onboard VM or container workloads with confidence. Control network and compute resources through hypervisor and container engine. Control storage capacity and QoS with SolidFire
- Never buy storage, compute and software that you don't need (a norm with _shared core_ HCI clusters)
- Probably the best HCI platform for migration of old vSphere 5.x clusters to a modern vSphere and container infrastructure
- Netapp HCI lets you repurpose your HCI compute nodes. VMware to OpenStack or the other way around, for example

## Resources and Solutions

- You may want to check out the official [catalog of NetApp HCI solutions](https://docs.netapp.com/us-en/hci/solutions/index.html). Even though some of the solutios may require NetApp HCI, a lot of that content also applies to SolidFire

### Cloud

- Synchronization to/from public cloud: Element OS supports SnapMirror (async) to/from [Cloud Volumes ONTAP](https://cloud.netapp.com/ontap-cloud) available in all major public clouds. See [NetApp TR-4641](https://www.netapp.com/us/media/tr-4641.pdf) for additional details

### Virtualization

#### VMware vSphere

- Check out VMware related material on the NetApp web site (Private cloud, VDI/EUC, GPU computing and more)
- vCenter Plugin for Element Software (used to be called "VCP") is built into NetApp HCI and may be installed in other vCenter servers you want to connect to separate NetApp HCI volumes. SolidFire users may get it from NetApp downloads for Element Software
- [vRealize Orchestrator Plugin for Element Software](https://github.com/solidfire/vrealize-orchestrator-plugin)
- [vRealize Automation for NetApp HCI and SolidFire](https://bluemedora.com/resource/vmware-vrealize-operations-management-pack-for-netapp-hci-solidfire/)
- [pyNSXdeploy](https://github.com/solidfire/pyNSXdeploy) -  automate deployment of NSX on vSphere 6.x on NetApp HCI

#### Microsoft Hyper-V

- PowerShell [scripts](https://github.com/solidfire/PowerShell/tree/release/1.5.1/Microsoft) for automated storage deployment with Microsoft Hyper-V (for Windows Server 2012 R2; requires minor updates for Microsoft Windows Server 2016 and 2019)
- [Solidfire VSS Provider](https://mysupport.netapp.com/products/p/elementvss.html) for MS Windows (login required)

#### Linux-related (OpenStack, KVM, XenServer, Oracle VM)

- Cinder driver for OpenStack (in-tree, does not need to be installed, it only needs to be configured)
- [Juju charm](https://github.com/solidfire/charm-cinder-solidfire) for Cinder to use Element cluster back end
- NetApp's [OpenStack resources and docs](https://netapp.io/openstack/)
- Redhat OpenShift with NetApp HCI - [NetApp Validated Design 1133](https://www.netapp.com/us/media/nva-1133-design.pdf)
- Recommended Deployment method for Redhat OpenStack on NetApp HCI is Ansible, but you may use PowerShell, Terraform or other approach to create SolidFire storage cluster

#### Storage Provisioning for Containers (CSI and Docker)

- [NetApp Trident](https://github.com/NetApp/trident) - CSI-compatible dynamic volume provisioner for container platforms (Docker, Kubernetes, Redhat OpenShift and others)
- Redhat OpenShift Container Platform. You can run it two ways: VM-based OCP VMs on vSphere or OpenStack clusters, or bare metal-based OCP on OpenStack clusters
- Docker and all [container orchestrators supported](https://netapp-trident.readthedocs.io/en/latest/support/requirements.html#supported-frontends-orchestrators) by NetApp Trident
- [NetApp Kubernetes Service](https://cloud.netapp.com/kubernetes-service): NetApp's Kubernetes-as-a-service is currently in preview on NetApp HCI (not yet stand-alone SolidFire)

### CLI, API, SDK Resources

#### CLI

- SolidFire has two fully functional CLI's - PowerShell & Python
  - SolidFire [PowerShell Tools (Win/Lin)](https://github.com/solidfire/PowerShell)
  - Solidfire [Python CLI (Win/Lin/OS X)](https://github.com/solidfire/solidfire-cli)

#### SolidFire/Element Software Development Kits (SDKs)

- [SolidFire Python SDK](https://github.com/solidfire/solidfire-sdk-python)
- [SolidFire Microsoft .NET SDK](https://github.com/solidfire/sdk-dotnet)
- [SolidFire Java SDK](https://github.com/solidfire/solidfire-sdk-java)
- [SolidFire Ruby SDK](https://github.com/solidfire/solidfire-sdk-ruby)
- [(Unofficial) SolidFire Go SDK](https://github.com/solidfire/solidfire-sdk-golang) and its cousin [solidfire-go](https://github.com/j-griffith/solidfire-go) with a convenient wrapper for common volume operations

### Automation

- Postman JSON [collection](https://github.com/solidfire/postman) for Element software

#### Automation and Configuration Tools and Frameworks

- [Ansible modules](https://docs.ansible.com/ansible/latest/search.html?q=NetApp+Element+Software) for Element Software (look for `na_elementsw_* modules`)
- [SolidFire Puppet plugin](https://github.com/solidfire/solidfire-puppet)
- [Terraform Plugin for SolidFire (unofficial)](https://github.com/solidfire/terraform-provider-solidfire) - works with Terraform v0.12
- [Terraform for NetApp Kubernetes Service on HCI](https://docs.netapp.com/us-en/kubernetes-service/intro-to-terraform-on-nks.html)

### Alerting, Monitoring, Telemetry

#### ActiveIQ

- Use ActiveIQ API to monitor your NetApp HCI or SolidFire cluster (requires valid support account)
- API docs - access Swagger upon login to ActiveIQ
- [NetApp ActiveIQ Documentation](https://docs.netapp.com/us-en/active-iq/)
- [ActiveIQ user portal](https://activeiq.solidfire.com) (login required)

#### NetApp Cloud Insights

- Enterprise-grade, professional infrastructure monitoring
- Cloud-hosted service, requires on-prem VM to acquire data and send it to your NeApp Cloud account
- A free version has basic functionality and supports all NetApp products including SolidFire and NetApp HCI

#### Grafana/Graphite - HCICollector

- [HCICollector](https://github.com/scaleoutsean/hcicollector/) is a permissively-licensed monitoring and alerting for SolidFire and NetApp HCI systems. It gathers SolidFire and vSphere 6.x metrics, stores them in Graphite and lets you visualize them in Grafana

#### Prometheus - solidfire-exporter

- [solidFire-exporter](https://github.com/mjavier2k/solidfire-exporter/) fetches and serves SolidFire metrics in the Prometheus format

#### Icinga and Nagios

- [elementOS-monitoring](https://github.com/aleex42/elementOS-monitoring) - more [here](https://blog.krogloth.de/nagios-icinga-monitoring-for-netapp-solidfire/)
- [nagfire](https://github.com/scaleoutsean/nagfire/) - supports both SolidFire cluster and individual nodes

#### SNMP MIBs

- SolidFire MIBs may be downloaded from the SolidFire/Element Web UI
- SNMP is disabled by default. If you enable it, you may choose v2 or v3
- Hardware MIBs may be available as well (check the NetApp KB for details relevant to your own hardware model(s))

#### Syslog Forwarding

- Forwarding to external syslog-ng target may be configured through a CLI or the API (see `SetRemoteLoggingHosts` method in Solidfire documentation)
- VMware-based NetApp HCI surfaces Element cluster events and alerts to vCenter; if ActiveIQ is enabled, these alerts are also sent to ActiveIQ

#### Event Notifications

- Users with existing notification solution: use Syslog forwarding or SNMP. You may also [integrate](https://www.youtube.com/watch?v=el2FBI0v27E) NetApp ActiveIQ with your existing system
- Users without an existing solution may consider one of these:
  - NetApp ActiveIQ: mobile app notifications (faster), email notifications (slower; enable them in the ActiveIQ Web UI)
  - Grafana: ([HCICollector](https://github.com/scaleoutsean/hcicollector) can send email notifications. Other Grafana methods may be used as well
  - Icinga and Nagios (email)

### Backup, Restore, Site Failover

- While you backup SolidFire by backing up front-end VMs or application data, the following vendors (ordered alphabetically) can integrate with SolidFire API to make backups better
  - Cleondris
  - Commvault
  - Veeam
- You can also replicate to, and then backup from ONTAP, which becomes attractive with large backup jobs: set up SolidFire SnapMirror to ONTAP with NL-SAS disks and backup the volume on ONTAP. When you have to backup a 20TB database on HCI, you'll be better off with NetApp HCI and ONTAP than with any other HCI
- DR
  - Native Synchronous and Asynchronous Replication - see NetApp TR-4741 or newer
  - Site failover
    - SolidFire SRA for VMware SRM

## Demo VM, Tools and Utilities

### SolidFire/Element Demo VM

- Element Demo VM: partners and customers may [download](https://mysupport.netapp.com/tools/info/ECMLP2848232I.html?pcfContentID=ECMLP2848232&productID=62139&pcfContentID=ECMLP2848232) (NetApp partner or support login required) and use it at no cost. Data and configuration persist after a reboot. It works with Kubernetes (Trident), VMware ESXi and other iSCSI clients supported by SolidFire
- NetApp OneCollect: this awesome and gratis multi-purpose utility that runs on Windows, Linux and in [Docker](https://hub.docker.com/r/netapp/onecollect/) containers is generally used for log data gathering but it can be used for configuration change tracking when set to run on schedule (watch [this video](https://www.youtube.com/watch?v=ksSs9wUi4sM) to get an idea - just don't run it in Element Management Node because that is not supported)

### Recorded Demos

- [Search YouTube for SolidFire](https://www.youtube.com/results?search_query=solidfire&sp=CAI%253D) and sort by most recent. Also check out [NetApp HCI](https://www.youtube.com/results?search_query=netapp+hci&sp=CAI%253D) video demos since NetApp HCI uses SolidFire storage

## Scripts and How-To Articles

### VMware

- PowerShell [Script](https://github.com/kpapreck/test-plan/blob/master/kp-clone-snap-to-datastore.ps1) to clone a VMFS6 volume from a SolidFire snapshot and import it to vCenter
- PowerShell [examples](https://github.com/solidfire/PowerShell/tree/release/1.5.1/VMware) for VMware
- PowerShell [scripts](https://github.com/solidfire/PowerShell/tree/release/1.5.1/SPBM) for integration with Storage Policy Based Management

Do not use old performance-tuning scripts from these examples on VMware ESXi 6.5 and above because they were written for ESXi 5.5 and 6.0. ESXi 6.5 and later have appropriate SolidFire MPIO settings built-in and require no special modification or tuning

### Windows

- PowerShell [scripts for Hyper-V 2012 R2](https://github.com/solidfire/PowerShell/tree/master/Microsoft) (need a refresh for Windows Server 2016 and 2019)

## Questions and Answers

### Meta

Q: Is information on this page correct, up-to-date and endorsed by NetApp?

A: Absolutely not. For official information please visit the NetApp Web sites (such as www.netapp.com and www.netapp.io)

Q: I have a quick question about ...

A: Please join [the NetApp community Slack](https://netapppub.slack.com/join/shared_invite/enQtNzc0MDAwNzQ5MDc2LTE4ZDQxODgwZmY3NGUwNWM2OGVkMDlkNjZjNTEzZDYwMDMwYWM1M2E4ZmNiNzYyMWE5NmVkYTMyODdlMzhhOTI) and ask your question in the `#netapp-hci` channel. If you need more eyes on the question or already have an account at the  [NetApp Community Forum](https://community.netapp.com/t5/AFF-NVMe-EF-Series-and-SolidFire-Discussions/bd-p/flash-storage-systems-discussions) please ask there and tag your question with 'solidfire'.

### Element Demo VM

Q: Is Element Demo VM a simulator?

A: No. It's a fully functional single-node SolidFire cluster. Due to the fact that it's a VM that runs on modest hardware resources, it has some limitations (no encryption, etc) which are documented at the download page. It is not supported for production.

Q: Can Element Demo VM be used to estimate efficiency from compression and deduplication?

A: It does compress and deduplicate, but I haven't compared how it fares against physical SolidFire clusters.

Q: Can I throw a couple of VMs on an Element Demo VM datastore to estimate how much I could save?

A: I believe it should be fairly accurate, but I haven't tested it. Get a representative sample of 5-10 VMs (up to 400GB combined) and clone them to an Element Demo VM-based test datastore. Give it a couple of hours to churn through that data and take a look.

### Hypervisors and Containers

Q: What hypervisor platforms work with SolidFire?

A: To be clear, this is about iSCSI clients supported by SolidFire storage (which may or may not be different from hypervisors supported by NetApp HCI compute hardware). You can find the official NetApp info with the [NetApp Interoperability Matrix Tool (IMT)](https://mysupport.netapp.com/matrix/#welcome) (look under Element software, not NetApp HCI!). The simple answer is NetApp HCI ships with VMware, but SolidFire (that is, iSCSI storage of NetApp HCI clusters) can work with other supported hypervisors. Some links to get you started with compatibility research:

- VMware ESXi - refer to the IMT
- Redhat OpenStack (KVM) - refer to the IMT
- MicroSoft Windows (Hyper-V) - search the WSC site (example for the [H615C](https://www.windowsservercatalog.com/item.aspx?idItem=4109a235-2b2e-3200-d3ef-065c8ea7c0c6&bCatID=1282))
- XenServer (Xen) - refer to the HCLs for [storage](http://hcl.xenserver.org/storage/?vendor=56) and [servers](http://hcl.xenserver.org/servers/?vendor=56)
- Oracle VM - go [here](https://linux.oracle.com/pls/apex/f?p=117:3::::::). Click on Storage Systems and in filter rop-down list select NetApp. Look for SolidFire models from the NetApp HCI Datasheet or Web site (for example, H610S)
- Other Linux distributions validated (Cinder iSCSI) for SolidFire Element OS - Ubuntu, SuSE, etc. (the details can be found in the IMT)

If unsure, contact NetApp with any questions or ask in the [NetApp Community Forum](https://community.netapp.com/t5/AFF-NVMe-EF-Series-and-SolidFire-Discussions/bd-p/flash-storage-systems-discussions) (free membership account required)

Q: Does SolidFire work with my Kubernetes?

A: If Trident works, SolidFIre works too. Some known supported distros are listed [here](https://netapp-trident.readthedocs.io/en/latest/support/requirements.html#supported-frontends-orchestrators) but other CSI-compatible distros should work as well (for example Rancher does). I recommend to check out Trident [issues](https://github.com/NetApp/trident/issues) as well to see if there's anything that you care about. Note that issues and requirements change between releases, so sometimes you may be better off with an older release in which case you shuold check supported requirements for older Trident releases.

### Workloads

Q: Should I use SolidFire with (or for) ...

A: It depends. At the highest level of abstraction SolidFire is suitable for 95% of apps people virtualize or containerize on on-premises x86_64 infrastructure. If you think you're a one percenter, you may want to discuss it with a SolidFire or Cloud Infrastructure architect. NetApp HCI may be able to accommodate even extreme workloads if you offload some data processing to external NFS or iSCSI storage such as NetApp AFF or E-Series.

Q: Is NetApp HCI suitable for AI, Hadoop, Splunk and similar "heavy" workloads?

A: For some applications from that stack (such as databases) it is, but for HDFS you may consider connecting compute nodes ONTAP hardware (see [NIPAM](https://pypi.org/project/netapp-ontap/)) or E-Series (Raw Device Mapping to iSCSI, formatted with HDFS or [BeeGFS](https://blog.netapp.com/solution-support-for-beegfs-and-e-series/), for example)

### Storage Services

Q: What protocols are supported?

A: For SolidlFire, it's iSCSI for x86_64 Linux, Windows and VMware hosts. No UNIX and no Fibre Channel. See the next question for NFS and SMB.

Q: Okay, I want SolidFire but what about NFS and SMB?

A: You can buy a software-based ONTAP license (NetApp ONTAP Select) and run it off your ESXi or KVM compute node(s). It's great for small to medium file servers, DevOps, K8s integrations, and data that needs to be replicated to or from major public clouds (where you'd have NetApp Cloud Volumes ONTAP). For file servers with large amounts of data that cannot be compressed or deduplicated, Big Data, volumes that need extreme performance (GB/s), consider connecting your servers to an E-Series (iSCSI) or ONTAP (iSCSI, NFS v3/v4/v4.1) storage - even when such workloads can run on SolidFire, it's usually not a good choice (price/performance-wise).

ONTAP Select running on NetApp HCI compute nodes can store its data either (or both) on NetApp HCI storage or external storage supported by hypervisor (ESXi 6.7, for example).

- [TR-4669](https://www.netapp.com/us/media/tr-4669.pdf): HCIFile Services Powered by ONTAP Select
- ONTAP Select [documentation](https://docs.netapp.com/us-en/ontap-select/)

### DevOps

Q: Where can I find some examples of SolidFire use in DevOps?

A: Check out SolidFire-related blog posts in [DevOps and Automation](https://netapp.io/devops/) category at [NetApp.io](https://netapp.io/). Ideally we should maximize automation by using a front-end orchestrator (vSphere, Kubernetes, and so on) rather than directly accessing storage, although the Element API makes that convenient and easy.

Q: When should I use the SolidFire API?

A: There are situations where certain operations may be done faster or more efficiently by talking directly to SolidFire API. Some examples:

- clone SolidFire volumes: automate, optimize or otherwise enhance your workflow
- set up replication relationships and/or failover procedures without having to rely on external integrations such as VMware SRM (SolidFire SRA)
- automate movement of data between VMware vRDM, Linux volumes and Docker containers
- speed up workflows by working directly with SolidFire API (Terraform plugin for SolidFire, SolidFire SDKs and CLIs)
- use an API method that's not (or not yet) exposed through a 3rd party integration (vCenter plugin) or even SolidFire SDK (for example, currently that is the case with Element storage Qos histograms)

Q: How can I use a feature that is availble but not exposed in a SolidFire SDK or API or CLI?

A: PowerShell Tools for SolidFire and all SDKs have a wrapper method (Invoke SF API) that simplifies the use of the API methods for which there is no cmdlet or direct method in an SDK. You can also use generic JSON RPC calls which may be a good choice for simple scripts in which you don't intend to use a SolidFire SDK because you don't want to install additional dependencies for simple projects.

### Networking

Q: What network switches are recommended for use with SolidFire?

A: I think there's no officially recommended switch model or brand. Any enterprise-grade 10G (or faster) switch should work. Some switches are better, some worse.
SolidFire can be ordered with Mellanox SN2010 switches (which work really well) and NetApp can deploy them and SolidFire for you (it usually takes just a couple of hours).

Q: Can I connect my FC SAN clients to SolidFire?

A: SolidFire and later NetApp used to sell a SolidFire Fibre Channel gateway node, but it's no longer available. I don't know what the official reason is, but I suspect fewer and fewer people use Fibre Channel in VI and now container environments. It's complex, hard to manage, expensive, and frankly unnecessary (not that FC itself is unnecessary, but in my opinion it's unnecessary for 95% of workloads people run in containers and virtual machines). The other reason is iSCSI works well and is also cheaper. Almost noone can work without Ethernet, but most people can work without FC, so... If you haven't considered iSCSI yet take a look at [TR-4367](https://www.netapp.com/us/media/tr-4367.pdf) created by ONTAP specialists, which provides a fairly recent comparison between NFS, iSCSI and FC.

## License and Trademarks

awesome-solidfire by scaleoutSean is licensed under the Do What The F*ck You Want To Public License (see LICENSE.md)

NetApp, ONTAP, SolidFire, SnapMirror and the marks listed at www.netapp.com/TM are trademarks of NetApp, Inc.
Redhat, Kubernetes, and other brands and marks belong to their respective owners.
