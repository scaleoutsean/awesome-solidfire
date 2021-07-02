# Awesome SolidFire: An Unofficial Collection of NetApp SolidFire Resources

- [Awesome SolidFire: An Unofficial Collection of NetApp SolidFire Resources](#awesome-solidfire-an-unofficial-collection-of-netapp-solidfire-resources)
  - [NetApp SolidFire-based Offerings](#netapp-solidfire-based-offerings)
    - [NetApp SolidFire All Flash Storage](#netapp-solidfire-all-flash-storage)
    - [NetApp Enterprise Software-Defined Storage (eSDS)](#netapp-enterprise-software-defined-storage-esds)
    - [NetApp HCI](#netapp-hci)
  - [Why SolidFire](#why-solidfire)
    - [Why NetApp HCI](#why-netapp-hci)
  - [Resources and Solutions](#resources-and-solutions)
    - [Cloud](#cloud)
    - [Virtualization](#virtualization)
      - [VMware vSphere](#vmware-vsphere)
      - [Microsoft Hyper-V](#microsoft-hyper-v)
      - [Red Hat Virtualization (RHEV)](#red-hat-virtualization-rhev)
      - [Citrix Hypervisor](#citrix-hypervisor)
      - [Linux-related (OpenStack, KVM, Oracle VM)](#linux-related-openstack-kvm-oracle-vm)
      - [Oracle VirtualBox](#oracle-virtualbox)
      - [Virtual Desktop Infrastructure and End User Computing (VDI & EUC)](#virtual-desktop-infrastructure-and-end-user-computing-vdi--euc)
    - [Kubernetes and Containers](#kubernetes-and-containers)
      - [Red Hat OpenShift Container Platform](#red-hat-openshift-container-platform)
      - [Rancher](#rancher)
      - [Google Anthos](#google-anthos)
      - [Docker CE and Mirantis Kubernetes Engine (MKE)](#docker-ce-and-mirantis-kubernetes-engine-mke)
    - [File-sharing (NFS, SMB)](#file-sharing-nfs-smb)
    - [CLI, API, SDK Resources](#cli-api-sdk-resources)
      - [API](#api)
      - [CLI](#cli)
      - [SolidFire/Element Software Development Kits (SDKs)](#solidfireelement-software-development-kits-sdks)
    - [Automation](#automation)
      - [Automation and Configuration Tools and Frameworks](#automation-and-configuration-tools-and-frameworks)
    - [Alerting, Monitoring, Telemetry](#alerting-monitoring-telemetry)
      - [ActiveIQ](#activeiq)
      - [NetApp Cloud Insights](#netapp-cloud-insights)
      - [VMware / Blue Medora True Visibility for VMware vRealize Operations](#vmware--blue-medora-true-visibility-for-vmware-vrealize-operations)
      - [VMware vRealize Log Insight](#vmware-vrealize-log-insight)
      - [Graylog](#graylog)
      - [ELK](#elk)
      - [Grafana/Graphite - HCICollector](#grafanagraphite---hcicollector)
      - [Grafana/Prometheus - solidfire-exporter](#grafanaprometheus---solidfire-exporter)
      - [Prometheus - NetApp Trident metrics](#prometheus---netapp-trident-metrics)
      - [Icinga and Nagios](#icinga-and-nagios)
      - [SNMP MIBs](#snmp-mibs)
      - [Splunk](#splunk)
      - [Syslog Forwarding](#syslog-forwarding)
      - [Security and General Auditing](#security-and-general-auditing)
      - [Event Notifications](#event-notifications)
    - [Backup, Restore, DR and BC (Site Failover)](#backup-restore-dr-and-bc-site-failover)
    - [Security](#security)
    - [Encryption](#encryption)
  - [Demo VM, Tools and Utilities](#demo-vm-tools-and-utilities)
    - [SolidFire/Element Demo VM](#solidfireelement-demo-vm)
    - [Recorded Demos](#recorded-demos)
  - [Scripts and How-To Articles](#scripts-and-how-to-articles)
    - [Generic](#generic)
    - [VMware](#vmware)
    - [Windows](#windows)
    - [SolidFire API-related details](#solidfire-api-related-details)
      - [SolidFire Objects](#solidfire-objects)
      - [Unique Object Names](#unique-object-names)
      - [Date and Time in SolidFire API](#date-and-time-in-solidfire-api)
  - [Questions and Answers](#questions-and-answers)
    - [Meta](#meta)
    - [SolidFire / Element Demo VM](#solidfire--element-demo-vm)
    - [Logging and Monitoring](#logging-and-monitoring)
    - [Hypervisors and Containers](#hypervisors-and-containers)
    - [Workloads](#workloads)
    - [Storage Services](#storage-services)
    - [DevOps](#devops)
    - [Networking](#networking)
  - [License and Trademarks](#license-and-trademarks)

## NetApp SolidFire-based Offerings

### NetApp SolidFire All Flash Storage

- SolidFire iSCSI storage clusters (available as storage-only clusters)
  - Shares storage nodes with the NetApp HCI product line
  - View all currently available models in 3D [here](https://apps.kaonadn.net/4817930843848704/index.html) (click on NetApp HCI))

### NetApp Enterprise Software-Defined Storage (eSDS)

- SolidFire Enterprise SDS (eSDS) - containerized enterprise Software Defined Storage for certified 3rd party hardware appliances
  - Apart from h/w monitoring and the OS (Red Hat, in this case), most features are nearly identical to SolidFire and NetApp HCI
  - Supports various 3rd party x86_64 servers
  - [Documentation](https://docs.netapp.com/us-en/element-software/index.html)
  - Ansible deployment scripts for eSDS: `nar_solidfire*` scripts [such as this one](https://github.com/NetApp/ansible/tree/master/nar_solidfire_sds_install). For non-eSDS (SolidFire appliances), you can use standard Element SW modules

### NetApp HCI

- NetApp HCI (NetApp HCI compute nodes connected via iSCSI to NetApp HCI storage nodes - some call it "disaggregated HCI" or dHCI)
  - View all currently available models in 3D [here](https://apps.kaonadn.net/4817930843848704/index.html) (click on NetApp HCI))

## Why SolidFire

- Fully programmable storage - from the initial node configuration to automated storage provisioning for containers
- Public Cloud-like, set-and-forget iSCSI storage for clients ranging from bare metal x86-64 servers to hypervisors, VMs and containers
- Always-on storage efficiency with zero-performance impact. Compression and deduplication cannot be disabled
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
- Probably the best HCI platform for easy migration of old vSphere clusters to a modern vSphere and container infrastructure, and keeping your options open (due to the ability to connect to external non-HCI storage, use 3rd party servers and use multiple hypervisors)
- Netapp HCI lets you repurpose your HCI compute nodes. VMware to OpenStack or the other way around, for example

## Resources and Solutions

- You may want to check out the official [catalog of NetApp HCI solutions](https://docs.netapp.com/us-en/hci/solutions/index.html). Even though some of the solutions may require NetApp HCI, a lot of that content also applies to SolidFire with 3rd party compute nodes (iSCSI clients) and networking
- Where to find more:
  - Products: look under NetApp HCI or (storage-only) SolidFire in the [list of NetApp storage products](https://www.netapp.com/us/products/a-z/index.aspx)
  - Availability of products and support: for General Availability, End of Availability (EOA, also known as end of Sale), End of Support (EOS) info go to NetApp Support, search by model and filter results by "Product Communique"

### Cloud

- Data synchronization to/from public cloud: Element OS supports NetApp SnapMirror (async) replication to/from [Cloud Volumes ONTAP](https://cloud.netapp.com/ontap-cloud) which is available on all major public clouds. See [NetApp TR-4641](https://www.netapp.com/us/media/tr-4641.pdf) for additional details
- Backup, restore and DR to cloud can be achieved by using 3rd party backup/restore and replication software that performs file-level data protection and replication

### Virtualization

#### VMware vSphere

- Check out VMware related material on the NetApp web site (Private cloud, VDI/EUC, GPU computing and more)
- vCenter Plugin for Element Software (used to be called "VCP") is built into NetApp HCI and may be installed in other vCenter servers you want to connect to separate NetApp HCI volumes. SolidFire users may get it from NetApp downloads for Element Software
- [Element SRA](https://www.vmware.com/resources/compatibility/search.php?deviceCategory=sra&details=1&partner=64,439&keyword=solidfire&page=1&display_interval=10&sortColumn=Partner&sortOrder=Asc) for VMware SRM 8.3
- [vRealize Orchestrator Plugin for Element Software](https://github.com/solidfire/vrealize-orchestrator-plugin)
- [vRealize Automation for NetApp HCI and SolidFire](https://bluemedora.com/resource/vmware-vrealize-operations-management-pack-for-netapp-hci-solidfire/)
- [pyNSXdeploy](https://github.com/solidfire/pyNSXdeploy) -  automate deployment of NSX on vSphere 6.x on NetApp HCI
- Datastore naming conventions:
  - Best use VMware SDDC conventions and have workflows and procedures that eliminate the possibility of duplicate names (both on SolidFire and VMware side)
  - Convention: `<location><az_id>-<pod_type><pod_id>-<datastore_type><datastore_id>` where `datastore_type` is `iscsi` and `datastore_id` is a 2 or 3 digit datastore ID (unrelated to SolidFire Volume ID)

#### Microsoft Hyper-V

- [solidfire-windows](https://github.com/scaleoutsean/solidfire-windows) - general notes on Windows Server 2019 Hyper-V with NetApp SolidFire
- PowerShell [scripts](https://github.com/solidfire/PowerShell/tree/release/1.5.1/Microsoft) for automated storage deployment with Microsoft Hyper-V (for Windows Server 2012 R2; requires minor updates for Microsoft Windows Server 2016+)
- [SolidFire VSS Provider](https://mysupport.netapp.com/products/p/elementvss.html) for MS Windows (login required)

#### Red Hat Virtualization (RHEV)

- Red Hat Virtualization [solution page](https://docs.netapp.com/us-en/hci-solutions/redhat_virtualization_solution_overview__netapp_hci_with_rhv.html)
- Red Hat OpenShift with NetApp HCI 
  - [NetApp Verfied Architecture 1133 (NVA-1133 DESIGN)](https://www.netapp.com/us/media/nva-1133-design.pdf) - design
  - [NetApp Verified Architecture 1133 (NVA_1133 DEPLOY)](https://www.netapp.com/us/media/nva-1133-deploy.pdf) - deployment
  - [Heat templates](https://github.com/NetApp/hci-solutions/tree/master/netapp-hci-heat-templates) for Redhat OpenStack

#### Citrix Hypervisor

- NetApp HCI with Citrix Hypervisor ([solution summary](https://docs.netapp.com/us-en/hci-solutions/citrix_executive_summary.html))

#### Linux-related (OpenStack, KVM, Oracle VM)

- Cinder driver for OpenStack (in-tree, does not need to be installed, it only needs to be configured - see NetApp TR-6420 or [this video](https://youtu.be/rW5ZTlyhm7U))
  - RHOSP16 certification: https://catalog.redhat.com/software/openstack/detail/2257111
- [Juju charm](https://github.com/solidfire/charm-cinder-solidfire) for Cinder to use Element cluster back-end (may need to be updated)
- NetApp's [OpenStack resources and docs](https://netapp.io/openstack/)
- [Oracle VM](https://linux.oracle.com/pls/apex/f?p=117:3::::::) (look under Storage Systems > NetApp)
- Additional details about SolidFire in Linux environments: [solidfire-linux](https://github.com/scaleoutsean/solidfire-linux/)

#### Oracle VirtualBox

- VirtualBox iSCSI initiator isn't officially supported but [it appears to work](https://youtu.be/EqxK-mT9Fxw) on both Linux and Windows (VirtualBox (host) iSCSI initiator for Windows seems prone to timeouts and I/O errors; it's better to use Linux or Windows initiators out of guest VMs)
- VirtualBox on top of OS-provisioned storage works as usual, as do supported VirtualBox guests with direct access to SolidFire iSCSI targets

#### Virtual Desktop Infrastructure and End User Computing (VDI & EUC)

- [VMware EUC/VDI with VMware Horizon View](https://docs.netapp.com/us-en/hci-solutions/nhci_euc_vmware.html)
- [Citrix Virtual Desktop and Virtual Apps](https://docs.netapp.com/us-en/hci-solutions/citrix_executive_summary.html)
- [Hybrid Cloud VDI with NetApp Virtual Desktop Service](https://docs.netapp.com/us-en/hci-solutions/hcvdivds_netapp_virtual_desktop_service_overview.html) - works with NetApp Global File Cache (GFC) for SMB

### Kubernetes and Containers

- [NetApp Trident](https://github.com/NetApp/trident) - CSI-compatible dynamic volume provisioner for container platforms (Docker, Kubernetes, Red Hat OpenShift, Rancher RKE and others)

#### Red Hat OpenShift Container Platform

- You can run it two ways: VM-based OCP VMs on vSphere, Red Hat Virtualization or OpenStack, and bare metal-based OCP on RHEL. See the [official solution page](https://docs.netapp.com/us-en/netapp-solutions/containers/rh-os-n_solution_overview.html#netapp-trident) for additional details

#### Rancher

- Rancher on NetApp HCI: See the official NetApp HCI solutions page for additional details. I have a personal site with notes on this solution from a SolidFire angle [here](https://scaleoutsean.github.io/solid-rancher)
- Provision Rancher K8s to NetApp HCI vSphere clusters from the CLI with [ez-rancher](https://github.com/NetApp/ez-rancher/)

#### Google Anthos

- Anthos is supported on vSphere clusters. See the official NetApp HCI solutions page for additional details

#### Docker CE and Mirantis Kubernetes Engine (MKE)

- Docker and other [container orchestrators supported](https://netapp-trident.readthedocs.io/en/latest/support/requirements.html#supported-frontends-orchestrators) by NetApp Trident
- Docker Swarm is not supported with SolidFire and Trident, but Mirantis Kubernetes Engine is. More [here](https://scaleoutsean.github.io/2021/05/02/mirantis-mke-netapp-trident-solidfire.html)

### File-sharing (NFS, SMB)

- NetApp ONTAP Select 9.8 (single node or HA, including Active-Active stretch clusters with one ONTAP Select VM and NetApp HCI cluster per each site ([Metrocluster SDS](https://docs.netapp.com/us-en/ontap-select/concept_ha_config.html))
- Read-only and read-write caching:
  - NFS (on-prem and hybrid cloud, read-only): NetApp ONTAP Select with [FlexCache](https://www.netapp.com/us/info/what-is-flex-cache.aspx)
  - SMB (hybrid cloud, read-write):
    - NetApp FlexCache (ONTAP Select 9.8+)
    - [NetApp Global File Cache](https://cloud.netapp.com/global-file-cache) running as edge node in Microsoft Windows VM, with core file service running in public cloud (Cloud Volumes ONTAP or Cloud Volumes Service). As indicated, you don't need ONTAP Select on NetApp HCI for this one

### CLI, API, SDK Resources

#### API

- SolidFire has versioned API which means you can run your "old" automation scripts against an older API endpoint of your choosing (e.g. API endpoint version 8.0 is still available and works (as of 12.2) despite SolidFire 8 no longer being supported)
- SolidFire / Element Software API Reference Guide: 
  - HTML: [v12.3](https://docs.netapp.com/us-en/element-software/api/index.html)

#### CLI

- SolidFire has two fully functional CLI's - PowerShell & Python
- Current releases: download with `pip` (Python 3) and `Install-Module` (PowerShell), or Github, or (for registered users) from [https://mysupport.netapp.com/site/tools](https://mysupport.netapp.com/site/tools) (search for 'element' in Tools)
- Older releases (work fine with latest Element, but connect to older API endpoints and use older API version):
  - SolidFire [PowerShell Tools (Win/Lin)](https://github.com/solidfire/PowerShell) for the x86_64 architecture. It's not officially supported, but module `SolidFire.Core` has been field-tested and found to work on ARM64 (PowerShell 6)
  - SolidFire [Python CLI (Win/Lin/OS X)](https://github.com/solidfire/solidfire-cli)

#### SolidFire/Element Software Development Kits (SDKs)

- Current releases: free download for registered users from [https://mysupport.netapp.com/site/tools](https://mysupport.netapp.com/site/tools) (search for 'element' in Tools); Python SDK can be installed from pip
- Releases:
  - [SolidFire Python SDK](https://github.com/solidfire/solidfire-sdk-python)
  - [SolidFire Microsoft .NET SDK](https://github.com/solidfire/sdk-dotnet)
  - [SolidFire Java SDK](https://github.com/solidfire/solidfire-sdk-java)
  - [SolidFire Ruby SDK](https://github.com/solidfire/solidfire-sdk-ruby)
  - [(Unofficial) SolidFire Go SDK](https://github.com/solidfire/solidfire-sdk-golang) and its cousin [solidfire-go](https://github.com/j-griffith/solidfire-go) with a convenient wrapper for common volume operations

### Automation

- Postman JSON [collection](https://github.com/solidfire/postman) for Element software

#### Automation and Configuration Tools and Frameworks

- [Ansible modules](https://galaxy.ansible.com/netapp/elementsw?extIdCarryOver=true&sc_cid=701f2000001OH7YAAW) for Element Software (`ansible-galaxy collection install netapp.elementsw`) or visit the [Github repo](https://github.com/ansible-collections/netapp.elementsw)
- [SolidFire Puppet plugin](https://github.com/solidfire/solidfire-puppet)
- [Terraform Provider for NetApp Element Software](https://github.com/NetApp/terraform-provider-netapp-elementsw) - supports resources IQN, VAG, account, volume
  - Install it directly from [Terraform registry](https://registry.terraform.io/providers/NetApp/netapp-elementsw/latest)

### Alerting, Monitoring, Telemetry

#### ActiveIQ

- Use ActiveIQ API to monitor your NetApp HCI or SolidFire cluster (requires valid support account)
- API documentation - access it via Swagger upon login to ActiveIQ
- [NetApp ActiveIQ Documentation](https://docs.netapp.com/us-en/active-iq/)
- [ActiveIQ user portal](https://activeiq.solidfire.com) (login required)

#### NetApp Cloud Insights

- Enterprise-grade, professional infrastructure monitoring
- Cloud-hosted service, requires on-prem VM to acquire data and send it to your NetApp Cloud Insights account
- The free version has basic functionality and supports all NetApp products including SolidFire and NetApp HCI
- Monitor performance and OPEX of all on-prem assets (NetApp- and non-NetApp-made) as well as in public clouds (find examples in NetApp [WP-7319](https://www.netapp.com/us/media/wp-7319.pdf))

#### VMware / Blue Medora True Visibility for VMware vRealize Operations

- True Visibility [product suite](https://bluemedora.com/products/vmware-vrealize-true-visibility/) (now part of VMware)
- See True Visibility for NetApp HCI and SolidFire [product documentation](https://support.bluemedora.com/s/article/User-Documentation-vRealize-Operations-Management-Pack-for-NetApp-HCI-SolidFire)

#### VMware vRealize Log Insight

- Log Insight [can serve (v8.1)](https://docs.vmware.com/en/vRealize-Log-Insight/8.1/com.vmware.log-insight.administration.doc/GUID-848E4804-3837-4D5E-956E-2216B17376AD.html) as destination for SolidFire logs

#### Graylog

- Redirect SolidFire log directly or indirectly (for example first to syslog-ng and from there forward to Graylog in the GELF format)

#### ELK

- Redirect SolidFire log to syslog-ng or LogStash or whatever, and from there to Elastic

#### Grafana/Graphite - HCICollector

- [HCICollector](https://github.com/scaleoutsean/hcicollector/) is a permissively-licensed monitoring and alerting for SolidFire and NetApp HCI systems. It gathers SolidFire and vSphere 6.x metrics, stores them in Graphite and lets you visualize them in Grafana
- Recommended for NetApp HCI with VMware

#### Grafana/Prometheus - solidfire-exporter

- [Solidfire Exporter](https://github.com/mjavier2k/solidfire-exporter/) fetches and serves SolidFire metrics in the Prometheus format
- Recommended for stand-alone SolidFire and Kubernetes
- Works within Kubernetes without changes

#### Prometheus - NetApp Trident metrics

- In v20.01 NetApp Trident delivered support for Prometheus metrics. A how-to is available [here](https://netapp.io/2020/02/20/prometheus-and-trident/)

#### Icinga and Nagios

- [ElementOS-Monitoring](https://github.com/aleex42/elementOS-monitoring) - more [here](https://blog.krogloth.de/nagios-icinga-monitoring-for-netapp-solidfire/)
- [nagfire](https://github.com/scaleoutsean/nagfire/) - supports status check of both SolidFire clusters and individual nodes (Python 3)

#### SNMP MIBs

- SolidFire MIBs may be downloaded from the SolidFire/Element Web UI. You can download the MIB files and open them to see what events and stats are gathered and sent by it
- SolidFire OID is 1.3.6.1.4.1.38091 (`.iso.org.dod.internet.private.enterprises.solidFire`)
- SNMP is disabled by default. If you enable it, you may choose v2 or v3
- Element API also lets you access essential hardware status information via API methods `GetIpmiInfo` and `GetIpmiConfig`

#### Splunk

- Redirect SolidFire log to a TCP port on Universal Forwarder or Indexer
- Send SNMP events to UF or Indexer. The MIB files can be downloaded from the SolidFire Web UI. If you redirect SolidFire syslog, you probably don't want to also send SNMP traps to Splunk

#### Syslog Forwarding

- SolidFire (or NetApp HCI or eSDS)
  - Forwarding to external syslog target may be configured through the CLI or the API (see `SetRemoteLoggingHosts` method). Element uses TCP and the log may be forwarded to one or more destinations. Sample lines from the log are provided further below
  - VMware-based NetApp HCI surfaces Element storage cluster events and alerts to vCenter; if ActiveIQ is enabled, these alerts are also sent to ActiveIQ
- mNode and NetApp Hybrid Cloud Control (HCC)
  - There are two components: mNode logs (rsyslog) and HCC (Docker service, in the current version). Both can be configured to forward logs to external syslog target (TCP or UDP). Only the former can forward to multiple destinations.
  - `GET /logs` from HCC may be used to obtain the logs of individual HCC services (containers), which Docker service currently does not forward. This could be coded into a "polling" script written in PowerShell or Python, for example. See the HCC API for more on using this API method or [this](https://scaleoutsean.github.io/2020/12/08/get-bearer-token-for-netapp-hci-hybrid-cloud-control-logs.html) article.

#### Security and General Auditing

- See Syslog Forwarding above
- Due to space constraints within SolidFire storage nodes and mNode, if longer log retention is required it is suggested to forward logs to external destination
- See [TR-4840](https://www.netapp.com/pdf.html?item=/media/19389-tr-4840.pdf) and SolidFire documentation for details on authentication and authorization (including MFA/2FA)
- White paper on [PCI DSS](https://www.coalfire.com/resources/white-papers/netapp-hci-verified-architecture-for-pci-dss) contains information for users with PCI DSS compliance requirements
- See the KMIP notes in this repo for practical notes on TLS certificates and KMIP

#### Event Notifications

- Users with existing notification solution: use Syslog forwarding or SNMP. You may also [integrate](https://youtu.be/aiwkKQaz7AQ) NetApp ActiveIQ with your existing monitoring application
- Users without an existing solution may consider one of these:
  - NetApp ActiveIQ: mobile app notifications (faster), email notifications (slower; enable them in the ActiveIQ Web UI)
  - Grafana: [HCICollector](https://github.com/scaleoutsean/hcicollector) and (Grafana in general) can send email notifications
  - Icinga and Nagios (email)

### Backup, Restore, DR and BC (Site Failover)

- While you backup SolidFire data by backing up front-end VMs or application data, the following vendors (ordered alphabetically) can integrate with SolidFire API to make data protection and business continuity easier and better
  - Cleondris HCC
  - Commvault
  - Rubrik
  - Veeam BR
- E/EF-Series (with iSCSI host interface) attached to NetApp HCI is ideal fast Tier 1 backup pool/storage (gigabytes per second). You can find indicators of backup and restore performance in [this blog post](https://scaleoutsean.github.io/2020/12/30/netapp-hci-ef280-diskspd-for-backup.html)
- Open-source integrations for non-CSI environments (Borg, Duplicati, Restic, Borg, etc.)
  - Snapshot, clone and mount SolidFire volumes, then use a backup utility to replicate clone to backup storage (E-Series, etc.) or S3 (NetApp StorageGRID, AWS S3, etc.)
  - Video demo with [Duplicati](https://youtu.be/wP8nAgFo8og)
  - Kubernetes users can use Velero (see below)
- You can also replicate to, and then backup from ONTAP, which becomes attractive with large backup jobs: set up SolidFire SnapMirror to an ONTAP system with NL-SAS disks and backup the volume on ONTAP. When you have to backup a 20TB database on HCI, you're better off backing it up with NetApp HCI replicated to ONTAP than directly from HCI (either NetApp or any other)
- DR for Virtual Infrastructure
  - Native Synchronous and Asynchronous Replication - see NetApp TR-4741 or newer
  - Site failover
    - SolidFire SRA for VMware SRM
    - Some of the backup offerings mentioned above provide functionality similar to VMware SRM
- CSI Trident with `solidfire-san` back-end
  - Can be backed up by creating thin clones and presenting them to a VM or container running a backup software agent (example with [Duplicacy](https://youtu.be/bvI7pgXKh6w))
  - Enterprise backup software can also backup Trident volumes. Examples in alphabetical order:
    - Commvault B&R: [documentation](https://documentation.commvault.com/11.21/essential/123637_system_requirements_for_kubernetes.html) and [demo](https://www.youtube.com/watch?v=kiMf9Fkhxd8). Metallic VM is another offering with this technology.
    - Kasten K10: [documentation](https://docs.kasten.io/latest/install/storage.html?highlight=netapp#netapp-trident) and [demo](https://www.youtube.com/watch?v=ShrSDwzQ0uU)
    - Velero: [documentation](https://github.com/vmware-tanzu/velero) and [demo](https://www.youtube.com/watch?v=6RrlK2rmk24). It can work both [with](https://github.com/vmware-tanzu/velero-plugin-for-csi) and without CSI. CSI support sort-of-works (CSI Plugin is currently beta quality, not yet production ready in Velero v1.5.3)
  - Storage cluster failover for Kubernetes with Trident CSI and two SolidFire clusters: use NetApp Trident's Volume Import feature (a quick demo (2m55s) can be viewed [here](https://youtu.be/aSFxlGoHgdA) while a deep-dive walk-through with a ton of detail can be found [here](https://scaleoutsean.github.io/2021/03/20/kubernetes-solidfire-failover-failback.html))

### Security

- Minimal security footprint - HTTPS (management interfaces) and iSCSI (storage) and on-demand SSH for remote support
- Multi-Factor Authentication (MFA) for management access (since v12.0)

### Encryption

- Uses SED drives with cluster-managed keys
- Supports KMIP-compatible external key managers (see the IMT for the current list of tested ISV solutions (HyTrust, [Thales SafeNet KeySecure](./encryption/kmip-thales-keysecure.md), etc.))
- FIPS 140-2 Level 2 certified SSDs (NetApp HCI H610S-2F model only)

## Demo VM, Tools and Utilities

### SolidFire/Element Demo VM

- Element Demo VM: partners and customers may [download](https://mysupport.netapp.com/tools/info/ECMLP2848232I.html?pcfContentID=ECMLP2848232&productID=62139&pcfContentID=ECMLP2848232) (NetApp partner or support login required) and use it at no cost. Data and configuration persist after a reboot. It works with Kubernetes (Trident), VMware ESXi and other iSCSI clients supported by SolidFire. 
  - SolidFire Demo VM can't be upgraded and scaled, but if you want to keep its data, you can stand up another one, set up async replication to a new instance and remove the old instance once replication is done. 
  - VMware users can simply Storage vMotion their data. I tend to Storage vMotion data to another DS (not new SolidFire Demo VM), remove VCP plugin from vCenter, remove Demo VM's iSCSI devices from any clients, delete the old Demo VM and deploy new VM in its place. Then I redeploy VCP (and register Demo VM in HCC, if I use it). The reason for doing things this way is I want to retain the same Storage and Management IP (which isn't easy to do if you use SolidFire replication to copy data from old to new Demo VM).
- NetApp OneCollect: this awesome and gratis multi-purpose utility that runs on Windows, Linux and in [Docker](https://hub.docker.com/r/netapp/onecollect/) containers is generally used for log data gathering but it can be used for configuration change tracking when set to run on schedule (watch [this video](https://www.youtube.com/watch?v=ksSs9wUi4sM) to get an idea - just don't run it on Element Management Node because that is not supported)

### Recorded Demos

- [Search YouTube for SolidFire](https://www.youtube.com/results?search_query=solidfire&sp=CAI%253D) and sort by most recent. Also check out [NetApp HCI](https://www.youtube.com/results?search_query=netapp+hci&sp=CAI%253D) video demos since NetApp HCI uses SolidFire storage

## Scripts and How-To Articles

### Generic

Find them in the `scripts` directory in this repo:

- `Set-SFQosException` - set "temporary" Storage Policy on a SolidFire volume
  - When Storage QoS Policy ID is passed to this cmdlet, it takes Volume's current Storage QoS Policy ID value, stores it in Volume Attributes, and sets Volume to user-provided "temporary" Storage QoS Policy ID
  - If Storage QoS Policy ID is not provided, it resets Volume to value stored in Volume Attributes
  - Can be used for any task that can benefit from short-lived change in volume performance settings. Written with SolidFire PowerShell Tools 1.6 and PowerShell 7 on Linux, but should work with PowerShell 6 or newer on Windows 10 or Windows Server 2016 or newer
- `Get-SFVolEff` - simple PowerShell script to list all volumes with storage efficiency below certain cut-off level (default: `2`, i.e. 2x)
- `parallel-backup-to-s3` - SolidFire-native Backup to S3
  - v1: runs `$p` parallel jobs to back up list of volumes identified by Volume ID (`$backup`) to an S3-compatible object store. The same script can be changed to restore in the same, parallel, fashion. Parallelization is over entire cluster - the script is not aware of per-node job maximums so aggressive parallelization may result in failed jobs that need to be resubmitted
  - v2: runs `$p` parallel jobs *per each node*, where $p is an integer between 0 and the maximum number of bulk jobs per node (8). It's made possible by `sfvid2nid` (below). You can read more about it [here](https://scaleoutsean.github.io/2021/06/22/solidfire-backup-and-cloning-with-per-storage-node-queues.html)
- `sfvid2nid` - SolidFire volume ID to node ID mapping script (PowerShell). This information can be used to drive the maximum per-node number of bulk volume jobs (such as built-in backup) and sync jobs (such as copy and clone volume jobs)

Some volume-cloning and backup-to-S3 scripts related to my SolidBackup concept can be found in the [SolidBackup repository](https://www.github.com/scaleoutsean/solidbackup).

### VMware

- SolidFire device names start with `naa.6f47acc1`
- PowerShell [script](https://github.com/kpapreck/test-plan/blob/master/kp-clone-snap-to-datastore.ps1) to clone a VMFS6 volume from a SolidFire snapshot and import it to vCenter
- PowerShell [examples](https://github.com/solidfire/PowerShell/tree/release/1.5.1/VMware) for VMware. Do not use old performance-tuning scripts from the SolidFire PowerShell repo. They were written for ESXi 5.5 and 6.0. ESXi 6.5 and later have appropriate SolidFire MPIO settings built-in and require no special modification or tuning

### Windows

- PowerShell [scripts for Hyper-V 2012 R2](https://github.com/solidfire/PowerShell/tree/master/Microsoft) (need a refresh for Windows Server 2016+)
- See the SolidFire Windows repo for some newer PowerShell scripts specific to SolidFire with Windows

### SolidFire API-related details

#### SolidFire Objects

- Many SolidFire objects - such as Volumes and Snapshots - can have custom attributes in the form of KV pairs
- We can employ attributes to tag a new volume like this:

```json
{
        "method": "CreateVolume",
        "params": {
                "name": "cvs_portal",
                "accountID": 2,
                "totalSize": 10240000000,
                "enable512e": "False",
                "attributes": {
                        "owner": "scaleoutSean",
                        "team": "operations"
                },
                "qosPolicyID": 1
        },
        "id": 1
}
```

- Not all environments assign ownership (tags) to teams or have the need to set attributes on SolidFire objects (for example, vSphere users can tag vSphere objects - they don't need to talk to SolidFire), but if they do, they can easily create reports and automate operations with only several lines of PowerShell
- Efficiency report for all volumes tagged with one such owner (empty volumes have the efficiency of 1X, if Thin Provisioning is not counted):

```powershell
PS > foreach ($vol in $(Get-SFVolume)){ if ($vol.Attributes.owner -eq "scaleoutSean"){Write-Host "Efficiency of Sean's Volumes:"`n "Volume ID:" $vol.VolumeID ; Get-SFVolumeEfficiency -VolumeID $vol.volumeID}}
Efficiency of Sean's Volumes:
 Volume ID: 57

Compression      : 1
Deduplication    : 1
MissingVolumes   : {}
ThinProvisioning : 1
Timestamp        : 1970-01-01T00:00:00Z
```

- Please do not confuse (storage) AccountID with the custom "owner" attribute above; large Kubernetes or Hyper-V cluster can use one AccountID for all Management OS, but volume "owners" can be many (or none, if the key is named differently or not at all used) and the latter is just a custom tag
- In Kubernetes, Docker and other orchestrated environments, pay attention to avoid the use of the same volume attribute keys used by NetApp Trident or other software that touches storage (such as Ansible, which stuffs KV pairs with keys such as "config-mgmt" and "event-source" into Attributes)
- NetApp ElementSW (SolidFire) modules for Ansible also set volume attributes since at least v20.10.0 (key names: `confg-mgmt` and `event-source`) so don't use those if you use Ansible with SolidFire and keep an eye on other objects

#### Unique Object Names

- SolidFire uses unique integer IDs to distinguish among most objects. While some Objects must have unique names, it is not the case for all Objects
- Main Object Names that can be non-unique: Volume, Volume Access Group, QoS Policy, Snapshot, Group Snapshot, Snapshot Schedule
  - It is strongly recommended to adopt a naming convention and avoid duplicate object names. Just because they're possible, it doesn't mean you should do it, especially if your management processes do not rely on Volume IDs 
- While it is a best practice to pick different names, SolidFire won't force you to do that, so either rely on Object IDs or stick to naming conventions for your environment or rely on Object IDs to distinguish among Objects. Note, however, that in the latter case any monitoring or other systems that use and display Names may malfunction or display confusing information

#### Date and Time in SolidFire API

- The SolidFire and HCC (Hybrid Cloud Control) APIs use [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) formatted UTC time.

## Questions and Answers

### Meta

Q: Is information on this page correct, up-to-date and endorsed by NetApp?

A: Absolutely not. For official information please visit the NetApp Web sites (such as www.netapp.com and www.netapp.io)

Q: I have a quick question about ...

A: Please join [the NetApp community Slack](https://join.slack.com/t/netapppub/shared_invite/zt-jdnzc1o7-Up1AIoNzZ4fEtONPG0_6Fw) and ask your question in the `#netapp-hci` channel. If you need more eyes on the question or already have an account at the  [NetApp Community Forum](https://community.netapp.com/t5/AFF-NVMe-EF-Series-and-SolidFire-Discussions/bd-p/flash-storage-systems-discussions) please ask there and tag your question with 'solidfire'.

### SolidFire / Element Demo VM

Q: Is Element Demo VM a simulator?

A: No. It's a fully functional single-node SolidFire cluster. Due to the fact that it's a VM that runs on modest hardware resources, it has some limitations (no encryption, etc) which are documented at the download page. It is not supported for production.

Q: Does Element Demo VM work on Virtualbox?

A: It's not supported, but version 12.3 works on Virtualbox 6.1 (find a demo on YouTube).

Q: Can Element Demo VM be used to estimate efficiency from compression and deduplication?

A: It does compress and deduplicate, but I haven't compared how it fares against physical SolidFire clusters.

Q: Can I throw couple of VMs on an Element Demo VM datastore to estimate how much I could save?

A: I believe that should be fairly accurate, but I haven't tested it. Get a representative sample of 5-10 VMs (up to 400GB combined) and clone them to an Element Demo VM-based test datastore. Give it a couple of hours to churn through that data and take a look.

### Logging and Monitoring

Q: I'd like to do something with SoliFire logs, how do SolidFire logs look like?

A: The following lines were obtained by forwarding SolidFire cluster log to syslog-ng (from which we can forward it elsewhere): the second is an API call and therefore in the JSON format). Element Software creates log using the rsyslog format (RFC-5424 and RFC-3164 (source: [Wikipedia](https://en.wikipedia.org/wiki/Rsyslog#Protocol)) and timestamps (format: `MMM  d HH:mm:ss`; RFC-3339). To make archived SolidFire logs more useful we'd have to create several filters (to gather only useful content and convert it to a format that's easier to analyse) somewhere along our log forwarding path. For comparison, vRealize Log Insight accepts formats in RFC-6587, RFC-5424, and RFC-3164 - see the Log Insight [link above](#vmware--blue-medora-true-visibility-for-vmware-vrealize-operations).

```shell
Jun  3 16:14:46 192.168.1.29 master-1[20395]: [APP-5] [API] 24018 DBCallback httpserver/RestAPIServer.cpp:408:operator()|Calling RestAPI::ListBulkVolumeJobs activeApiThreads=1 totalApiThreads=16 user=admin authMethod=Cluster sourceIP=192.168.1.12
Jun  3 16:14:46 192.168.1.29 master-1[20395]: {"action":"ApiCall","idg":"1775127282990285","idx":294566,"system":"Cluster","utc":"2020-06-03T16:14:46.058806Z","ver":"1.1","xClusterApiCall":{"AuthMthd":"Cluster","Method":"ListSyncJobs","SourceIP":"192.168.1.12","Threads":1,"Time":3,"TotalThreads":16,"Username":"admin"}}
```

Q: How can I get mNode and HCC logs?

A: Simple answer: forward mNode VM syslog out, and use the mNode API to get HCC logs. The details can be found [here](https://scaleoutsean.github.io/2020/11/27/solidfire-mnode-hcc-log-forwarding.html).

### Hypervisors and Containers

Q: What hypervisor platforms work with SolidFire?

A: To be clear, this is about iSCSI clients supported by SolidFire storage (which may or may not be different from hypervisors supported by NetApp HCI compute hardware). You can find the official NetApp info with the [NetApp Interoperability Matrix Tool (IMT)](https://mysupport.netapp.com/matrix/#welcome) (look under Element software, not NetApp HCI!). The simple answer is NetApp HCI ships with VMware, but SolidFire (that is, the iSCSI storage component of NetApp HCI) can work with other supported hypervisors (even at the same time). Some links to get you started with compatibility research:

- VMware ESXi - refer to the IMT
- Redhat OpenStack and Enterprise Virtualization - refer to the IMT
- MicroSoft Windows (Hyper-V) - search the WSC site (example for the [H615C](https://www.windowsservercatalog.com/item.aspx?idItem=4109a235-2b2e-3200-d3ef-065c8ea7c0c6&bCatID=1282))
- Citrix Hypervisor (formerly known as XenServer) - v8 is supported as per NetApp HCI VDI Solution with Citrix Hypervisor; for v7 refer to the HCLs for [storage](http://hcl.xenserver.org/storage/?vendor=56) and [servers](http://hcl.xenserver.org/servers/?vendor=56)
- Oracle VM - go [here](https://linux.oracle.com/pls/apex/f?p=117:3::::::). Click on Storage Systems and in filter rop-down list select NetApp. Look for SolidFire models from the NetApp HCI Datasheet or Web site (for example, H610S)
- Other Linux distributions validated (Cinder iSCSI) for SolidFire Element OS - Ubuntu, SuSE, etc. (the details can be found in the NetApp IMT)
- Oracle Virtualbox - not suported (as it uses its own iSCSI client that isn't validated by NetApp) but it works and you may want to use it in lab environment

If unsure, contact NetApp with any questions or ask in the [NetApp Community Forum](https://community.netapp.com/t5/AFF-NVMe-EF-Series-and-SolidFire-Discussions/bd-p/flash-storage-systems-discussions) (free membership account required)

Q: Does SolidFire work with my Kubernetes?

A: If Trident works with it, SolidFire can too. Some K8s distributions known to work are listed [here](https://netapp-trident.readthedocs.io/en/latest/support/requirements.html#supported-frontends-orchestrators) but other CSI-compatible distros should work as well. I recommend to check out Trident [issues](https://github.com/NetApp/trident/issues) as well to see if there's anything that you care about. Note that issues and requirements change between releases, so sometimes you may be better off with an older release in which case you shuold check supported requirements for older Trident releases.

### Workloads

Q: Should I use SolidFire with (or for) ...

A: It depends. At the highest level of abstraction SolidFire is suitable for 95% of apps people virtualize or containerize on on-premises x86_64 infrastructure. If you think you're "one percenter", you may want to discuss your requirements with a NetApp SolidFire or Cloud Infrastructure architect. NetApp HCI may be able to accommodate even extreme workloads if data processing to external NFS or iSCSI storage such as NetApp AFF or E-Series (see [NVA-1152-DESIGN](https://www.netapp.com/pdf.html?item=/media/21016-nva-1152-design.pdf)). Some HCI vendors force such storage workloads on their HCI storage which doesn't work well (or sort-of-works, but at a much higher price).

Q: Is NetApp HCI suitable for AI, Splunk, Elasticsearch and similar "heavy" workloads?

A: For some applications from that stack (such as databases) it is, but for HDFS you may consider connecting compute nodes to ONTAP systems (usually NFSv3 or NFSv4) or E-Series (physical Raw Device Mapping (pRDM) to iSCSI, formatted with HDFS or [BeeGFS](https://blog.netapp.com/solution-support-for-beegfs-and-e-series/), for example.) [NVA-1152-DESIGN](https://www.netapp.com/pdf.html?item=/media/21016-nva-1152-design.pdf) shows how adding the smallest EF-Series model can add 5 GB/s of throughput to NetApp HCI clusters without any investment in FC switches or new HCI compute nodes.

  - [This post](https://scaleoutsean.github.io/2020/12/31/beegfs-on-netapp-hci-and-ef-series.html) demonstrates few GB/s with BeeGFS VMs (single HCI compute node attached to EF-Series EF280)
  - Performance guesstimates for [Splunk](https://scaleoutsean.github.io/2020/12/31/virtualized-splunk-on-netapp-hci-and-ef-series.html) and [Elasticsearch](https://scaleoutsean.github.io/2021/01/04/elasticsearch-on-netapp-h615c-ef280.html)

### Storage Services

Q: What protocols are supported?

A: For SolidlFire, it's iSCSI for x86_64 Linux, Windows and VMware hosts. No UNIX and no Fibre Channel. See the next question for NFS and SMB.

Q: Okay, I want SolidFire but what about NFS and SMB?

A: You can buy a software-based ONTAP license (NetApp ONTAP Select) and run it off your ESXi or KVM compute node(s). It's great for small to medium file servers, DevOps, K8s integrations, and data that needs to be replicated to or from major public clouds (where you'd have NetApp Cloud Volumes ONTAP). For file servers with large amounts of data that cannot be compressed or deduplicated, Big Data, volumes that need extreme performance (GB/s), consider connecting your servers to an E-Series (iSCSI) or ONTAP (iSCSI, NFS v3/v4/v4.1) storage - even when such workloads can run on SolidFire, it's usually not a good choice (price/performance-wise).

ONTAP Select running on NetApp HCI compute nodes can store its data either (or both) on NetApp HCI storage or external storage supported by hypervisor (ESXi 6.7, for example).

- NetApp [TR-4669](https://www.netapp.com/us/media/tr-4669.pdf): HCI File Services Powered by ONTAP Select
- NetApp ONTAP Select [documentation](https://docs.netapp.com/us-en/ontap-select/)

### DevOps

Q: Where can I find some examples of SolidFire use in DevOps?

A: Check out SolidFire-related blog posts in [DevOps and Automation](https://netapp.io/devops/) category at [NetApp.io](https://netapp.io/). Ideally we should maximize automation by using a front-end orchestrator (vSphere, Kubernetes, and so on) rather than directly accessing storage, although the Element API makes that convenient and easy. Each SDK or CLI has documentation which contains some examples on getting started and the same goes for various Github repositories such as SolidiFire/Element Provider for Terraform.

Q: When should I use the SolidFire API?

A: There are situations where certain operations may be done faster or more efficiently by talking directly to SolidFire API. Some examples:

- clone SolidFire volumes: automate, optimize or otherwise enhance your workflow
- set up replication relationships and/or failover procedures without having to rely on external integrations such as VMware SRM (SolidFire SRA)
- automate movement of data between VMware vRDM, Linux volumes and Docker containers
- speed up workflows by working directly with SolidFire API (Terraform plugin for SolidFire, SolidFire SDKs and CLIs)
- use an API method that's not (or not yet) exposed through a 3rd party integration (vCenter plugin) or even SolidFire SDK (for example, currently that is the case with Element storage Qos histograms)

Q: How can I use a feature that is availble but not exposed in a SolidFire SDK or API or CLI?

A: PowerShell Tools for SolidFire and all SDKs have a wrapper method (Invoke SF API) that simplifies the use of the API methods for which there is no cmdlet or direct method in an SDK. You can also use generic JSON RPC calls which may be a good choice for simple scripts in which you don't intend to use a SolidFire SDK because you don't want to install additional dependencies for simple projects.

Q: How can I find the limits - say the maximum number of volumes - of my SolidFire cluster?

A: To get most if not all software-related limits use the API (`GetLimits`) or a CLI equivalent. For example, assuming `$MVIP` is the cluster management virtual IP, with SolidFire Powershell Tools `$sf = Connect-SFCluster $MVIP; $sf.limits` would do it. Note that there may be hardware-related limits or best practices that limit or impact overall cluster limits.

Q: Is there a quick way to try SolidFire PowerShell Tools or SolidFire Python CLI from Docker?

A: Yes. Sample Ubuntu-based container with SolidFire PowerShell Tools can be started with `docker run -it scaleoutsean/solidshell` (run `Connect-SFCluster` once inside). You can also build your own and include 3rd party PowerShell or Python modules you commonly use.

### Networking

Q: What network switches are recommended for use with SolidFire?

A: I think there's no officially recommended switch model or brand. Any enterprise-grade 10G (or faster) switch should work. Some switches are better, some worse.
SolidFire can be ordered with Mellanox SN2010 switches (which work really well) and NetApp can deploy them and SolidFire for you (it usually takes just a couple of hours). Also available are SN2100 and SN2700.

Q: What 4x25GBE copper and fiber breakout cables are available for NetApp HCI with SN2100 and SN2700?

Consider using these:

- [MFA7A50](https://www.mellanox.com/related-docs/prod_cables/PB_MFA7A50-Cxxx_100GbE_QSFP28_to_4x25GbE_SFP28_MMF_AOC.pdf)
- [MCP7F00](https://www.mellanox.com/related-docs/prod_cables/PB_MCP7F00-A0xxRyyz_100GbE_QSFP28_to_4x25GbE_4xSFP28_DAC_Splitter.pdf)

Q: Can I connect my FC SAN clients to SolidFire?

A: SolidFire and later NetApp used to sell SolidFire Fibre Channel gateway node, but it's no longer sold. I don't know what the official reason was, but I suspect fewer and fewer people use Fibre Channel in VI and now container environments. It's complex, hard to manage, expensive, and frankly unnecessary (not that FC itself is unnecessary for everyone, but in my opinion it's unnecessary for 95% of workloads people run in containers and virtual machines). The other reason is iSCSI works well and is also cheaper. Almost no one can work without Ethernet, but most people can work without FC, so if two links will do, why use four... If you haven't considered iSCSI yet take a look at [TR-4367](https://www.netapp.com/us/media/tr-4367.pdf) created by ONTAP specialists, which provides a fairly recent comparison between NFS, iSCSI and FC.

Q: Can the H600S series nodes enable LLDP on the management interface?

A: You can try to enable LLDP with `ipmitool raw 0x30 0xD1 0x0a` (starts within 10 seconds or so). To disable: `ipmitool raw 0x30 0xD1 0x00`.

## License and Trademarks

awesome-solidfire by scaleoutSean is licensed under the Do What The F*ck You Want To Public License (see [LICENSE](LICENSE))

NetApp, ONTAP, SolidFire, SnapMirror and the marks listed at www.netapp.com/TM are trademarks of NetApp, Inc.
Redhat, Kubernetes, and other brands and marks belong to their respective owners.
