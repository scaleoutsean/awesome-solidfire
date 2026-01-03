# Awesome SolidFire: An Unofficial Collection of NetApp SolidFire Resources

- [Awesome SolidFire: An Unofficial Collection of NetApp SolidFire Resources](#awesome-solidfire-an-unofficial-collection-of-netapp-solidfire-resources)
  - [NetApp SolidFire-based Offerings](#netapp-solidfire-based-offerings)
    - [End-of-Availability announcements](#end-of-availability-announcements)
    - [NetApp SolidFire All Flash Storage](#netapp-solidfire-all-flash-storage)
    - [NetApp Enterprise Software-Defined Storage (eSDS)](#netapp-enterprise-software-defined-storage-esds)
  - [Why SolidFire](#why-solidfire)
  - [Resources and Solutions](#resources-and-solutions)
    - [Cloud](#cloud)
    - [Virtualization](#virtualization)
      - [VMware vSphere](#vmware-vsphere)
      - [Microsoft Hyper-V](#microsoft-hyper-v)
      - [Red Hat Virtualization (RHEV)](#red-hat-virtualization-rhev)
      - [Citrix Hypervisor and XCP-ng](#citrix-hypervisor-and-xcp-ng)
      - [Proxmox (PVE)](#proxmox-pve)
      - [Linux-related (OpenStack, KVM, Oracle VM)](#linux-related-openstack-kvm-oracle-vm)
      - [Oracle VirtualBox](#oracle-virtualbox)
      - [Virtual Desktop Infrastructure and End User Computing (VDI \& EUC)](#virtual-desktop-infrastructure-and-end-user-computing-vdi--euc)
    - [Kubernetes and Containers](#kubernetes-and-containers)
      - [Get started with SolidFire](#get-started-with-solidfire)
      - [CSI Provisioners](#csi-provisioners)
      - [SolidFire Operator for Kubernetes](#solidfire-operator-for-kubernetes)
      - [Red Hat OpenShift Container Platform](#red-hat-openshift-container-platform)
      - [Rancher](#rancher)
      - [Flatcar Container Linux](#flatcar-container-linux)
      - [Google Anthos](#google-anthos)
      - [Docker CE and Mirantis Kubernetes Engine (MKE)](#docker-ce-and-mirantis-kubernetes-engine-mke)
      - [Platform9 Managed Kubernetes (PMK)](#platform9-managed-kubernetes-pmk)
      - [VMware Photon 4.0](#vmware-photon-40)
      - [KubeVirt (and OCPv)](#kubevirt-and-ocpv)
      - [HashiCorp Nomad](#hashicorp-nomad)
    - [File-sharing (NFS, SMB)](#file-sharing-nfs-smb)
    - [CLI, API, SDK Resources](#cli-api-sdk-resources)
      - [API](#api)
      - [API Gateways](#api-gateways)
      - [CLI](#cli)
      - [SolidFire/Element Software Development Kits (SDKs)](#solidfireelement-software-development-kits-sdks)
    - [Automation](#automation)
      - [Model Context Protocol](#model-context-protocol)
      - [Automation and Configuration Tools and Frameworks](#automation-and-configuration-tools-and-frameworks)
    - [Alerting, Monitoring, Telemetry](#alerting-monitoring-telemetry)
      - [ActiveIQ](#activeiq)
      - [NetApp Cloud Insights](#netapp-cloud-insights)
      - [VMware / Blue Medora True Visibility for VMware vRealize Operations](#vmware--blue-medora-true-visibility-for-vmware-vrealize-operations)
      - [VMware vRealize Log Insight](#vmware-vrealize-log-insight)
      - [Graylog](#graylog)
      - [Elasticsearch (ELK stack)](#elasticsearch-elk-stack)
      - [InfluxDB v3 - SolidFire Collector (SFC) v2](#influxdb-v3---solidfire-collector-sfc-v2)
      - [Graphite - HCI Collector v0.7.x](#graphite---hci-collector-v07x)
      - [Prometheus - solidfire-exporter](#prometheus---solidfire-exporter)
      - [Telegraf](#telegraf)
      - [Prometheus - NetApp Trident metrics](#prometheus---netapp-trident-metrics)
      - [Icinga and Nagios](#icinga-and-nagios)
      - [SNMP and SolidFire MIBs](#snmp-and-solidfire-mibs)
      - [Splunk](#splunk)
      - [Syslog Forwarding](#syslog-forwarding)
      - [Security and General Auditing](#security-and-general-auditing)
      - [ServiceNow integration](#servicenow-integration)
      - [Zabbix](#zabbix)
      - [Event Notifications](#event-notifications)
    - [Replication, DR and BC (Site Failover)](#replication-dr-and-bc-site-failover)
      - [Storage replication management with Longhorny, a SolidFire replication management tool (OSS)](#storage-replication-management-with-longhorny-a-solidfire-replication-management-tool-oss)
    - [Backup and Restore](#backup-and-restore)
      - [Built-in backup to S3](#built-in-backup-to-s3)
      - [VM and Bare Metal workloads](#vm-and-bare-metal-workloads)
      - [Trident CSI with `solidfire-san` back-end](#trident-csi-with-solidfire-san-back-end)
    - [Security](#security)
    - [Encryption](#encryption)
      - [Post-Quantum Cryptography](#post-quantum-cryptography)
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
      - [Date and Time Format in SolidFire API Responses](#date-and-time-format-in-solidfire-api-responses)
      - [Miscallenea](#miscallenea)
  - [Questions and Answers](#questions-and-answers)
    - [Meta](#meta)
    - [SolidFire / Element Demo VM](#solidfire--element-demo-vm)
    - [Logging and Monitoring](#logging-and-monitoring)
    - [Hypervisors and Containers](#hypervisors-and-containers)
    - [Workloads](#workloads)
    - [Storage Services](#storage-services)
    - [DevOps](#devops)
    - [iSCSI](#iscsi)
    - [Networking](#networking)
  - [License and Trademarks](#license-and-trademarks)


## NetApp SolidFire-based Offerings

### End-of-Availability announcements

- SolidFire: End of Sale was in 2023; see [CPC-00467](https://mysupport.netapp.com/info/communications/ECMLP2884466.html) for more (NetApp support portal login required)
  - Support is available until EOS + 5Y (late 2028). Please refer to the official NetApp Support site for details
- NetApp HCI: End of Sale was announced in Q1/CY21 and took effect in Q2/CY22
  - Support is available until EOS + 5Y (2027). Please refer to the official NetApp Support site for details
  - A growing number of links may become dead, but it's better to leave them (I think) since you may be able to get the content from Web Archive or similar sites

### NetApp SolidFire All Flash Storage

- SolidFire iSCSI storage clusters (available as storage-only clusters)
  - In NetApp HCI, SolidFire shares storage nodes with the NetApp HCI compute nodes and non-NetApp HCI compute nodes
  - You may view currently available SolidFire appliances [here](https://www.netapp.com/data-storage/solidfire/) or check which DellEMC, HPE or other servers are certified for [SolidFire eSDS](https://docs.netapp.com/us-en/element-software/esds/concept_get_started_esds.html)

### NetApp Enterprise Software-Defined Storage (eSDS)

- SolidFire Enterprise SDS (eSDS) - containerized enterprise Software Defined Storage for certified 3rd party hardware appliances
  - Apart from h/w monitoring and the OS (Red Hat, in this case), most features are nearly identical to SolidFire
  - Supports various 3rd party x86_64 servers
  - [Documentation](https://docs.netapp.com/us-en/element-software/index.html)
  - Ansible deployment scripts for eSDS: `nar_solidfire*` scripts [such as this one](https://github.com/NetApp/ansible/tree/master/nar_solidfire_sds_install). For non-eSDS (SolidFire appliances), you can use standard Element SW modules

## Why SolidFire

- Fully programmable storage - from initial node configuration to automated storage provisioning for containers
- Public Cloud-like, set-and-forget iSCSI storage for clients ranging from bare metal x86-64 servers to hypervisors, VMs and containers
- Always-On storage efficiency with zero-performance impact. Compression and deduplication cannot be disabled (see [these notes](https://scaleoutsean.github.io/2024/02/29/ubuntu-2404-lts-with-netapp-solidfire.html) on considerations for using compressed filesystems with SolidFire)
- Granular storage capacity and performance management - Minimum, Maximum and Burst storage policies may be assigned on a per-volume basis
- General purpose scale-out storage clusters that are easy to provision, manage, refresh, and scale
- Availability Zone-like data partitioning for rack, floor, campus environments (SolidFire Protection Domains)
- Can be merged into or serve as a base for NetApp HCI - add two or more NetApp HCI compute nodes and convert your SolidFire cluster into NetApp HCI

This animation shows some key (storage-, not performance-related) concepts:

- start with 4 or more nodes and expand with 1 or or more at once
- shrink the cluster by removing old nodes
- with Protection Domains (PDs), the failure of Rack 3 shown in animation doesn't cause downtime
- the way PDs, and SolidFire in general, works there are no RAID groups and all blocks are spread across the cluster (replicated twice, and balanced among multiple nodes and PDs, if the latter are available)

![SolidFire scale out, rebalancing and h/w refresh](/images/solidfire-scale-out-refresh.svg)

Volume placement considers both performance and capacity utilization:

- Volume placement depends on storage QoS settings, performance utilization, volume fullness and other factors
- Volume rebalancing happens transparently as these settings and conditions change - volumes get fuller or emptier, storage QoS settings get adjusted up or down, etc.
- As new hosts and volumes come online, they are placed optimally considering volume QoS settings and capacity and performance utilization of volumes

![SolidFire performance and metadata rebalancing](/images/solidfire-perf-and-md-rebalancing.svg)

## Resources and Solutions

- Products: look under NetApp HCI or (storage-only) SolidFire in the [list of NetApp storage products](https://www.netapp.com/us/products/a-z/index.aspx)
- Availability of products and support: for General Availability, End of Availability (EOA, also known as end of Sale), End of Support (EOS) info go to NetApp Support, search by model and filter results by "Product Communique"

### Cloud

- Data synchronization to/from public cloud: Element OS supports NetApp SnapMirror (async) replication to/from [Cloud Volumes ONTAP](https://cloud.netapp.com/ontap-cloud) which is available on all major public clouds. See [NetApp TR-4641](https://www.netapp.com/us/media/tr-4641.pdf) for additional details
- Backup, restore and DR to cloud can be achieved by using 3rd party backup/restore and replication software that performs file-level data protection and replication

### Virtualization

#### VMware vSphere

- Check out VMware related material on the NetApp web site (Private cloud, VDI/EUC, GPU computing and more)
- vCenter Plugin for Element Software (used to be called "VCP") is built into NetApp HCI and may be installed in other vCenter servers you want to connect to separate NetApp HCI volumes. SolidFire users may get it from NetApp downloads for Element Software
- [VMware Storage/SAN Compatibility Page](https://www.vmware.com/resources/compatibility/search.php?deviceCategory=san&details=1&partner=439&arrayTypes=1&isSVA=0&page=1&display_interval=10&sortColumn=Partner&sortOrder=Asc) for SolidFire iSCSI storage
- [Element SRA](https://www.vmware.com/resources/compatibility/search.php?deviceCategory=sra&details=1&partner=64,439&keyword=solidfire&page=1&display_interval=10&sortColumn=Partner&sortOrder=Asc) for VMware SRM 8.3
- [vRealize Orchestrator Plugin for Element Software](https://github.com/solidfire/vrealize-orchestrator-plugin)
- vRealize Automation for NetApp HCI and SolidFire (formerly BlueMedora packages)
- [pyNSXdeploy](https://github.com/solidfire/pyNSXdeploy) -  automate deployment of NSX on vSphere 6.x on NetApp HCI
- Datastore naming conventions:
  - Best use VMware SDDC conventions and have workflows and procedures that eliminate the possibility of duplicate names (both on SolidFire and VMware side)
  - Convention: `<location><az_id>-<pod_type><pod_id>-<datastore_type><datastore_id>` where `datastore_type` is `iscsi` and `datastore_id` is a 2 or 3 digit datastore ID (unrelated to SolidFire Volume ID)

#### Microsoft Hyper-V

- [solidfire-windows](https://github.com/scaleoutsean/solidfire-windows) - general notes on Windows Server 2019 Hyper-V with NetApp SolidFire
- PowerShell [scripts](https://github.com/solidfire/PowerShell/tree/release/1.5.1/Microsoft) for automated storage deployment with Microsoft Hyper-V (for Windows Server 2012 R2; requires minor updates for Microsoft Windows Server 2016+).
- [SolidFire VSS Provider](https://mysupport.netapp.com/products/p/elementvss.html) for MS Windows (login required)
  - Not available for recent Windows Server, but VSS hardware provider is practically no longer necessary - since SQL Server 2022 snapshots can be taken without it and on-prem MS Exchange is dead, which leave almost no applications that need it. See my Windows Server 2025 Preview notes in [solidfire-windows](https://github.com/scaleoutsean/solidfire-windows)

#### Red Hat Virtualization (RHEV)

- Red Hat Virtualization [solution page](https://docs.netapp.com/us-en/hci-solutions/redhat_virtualization_solution_overview__netapp_hci_with_rhv.html)
- Red Hat OpenShift with NetApp HCI 
  - [NetApp Verfied Architecture 1133 (NVA-1133 DESIGN)](https://www.netapp.com/us/media/nva-1133-design.pdf) - design
  - [NetApp Verified Architecture 1133 (NVA_1133 DEPLOY)](https://www.netapp.com/us/media/nva-1133-deploy.pdf) - deployment
  - [Heat templates](https://github.com/NetApp/hci-solutions/tree/master/netapp-hci-heat-templates) for Redhat OpenStack
- [Rocky Linux](https://rockylinux.org/) 8.6 and 9.0 and other downstream distributions should work the same way. Here's an example with [Trident Docker volume plugin](https://scaleoutsean.github.io/2022/08/21/rocky-linux-docker-netapp-trident-solidfire.html)

#### Citrix Hypervisor and XCP-ng

- Open-source fork [XCP-ng with SolidFire 12](https://scaleoutsean.github.io/2022/07/10/xcp-ng-with-netapp-solidfire-iscsi.html) as well as XOA
- NetApp HCI with Citrix Hypervisor ([solution summary](https://docs.netapp.com/us-en/hci-solutions/citrix_executive_summary.html))

#### Proxmox (PVE)

- Lightly tested with PVE version 9.1 and more extensively with PVE version 8.4 (SolidFire 12.5)
- Firemox - an opinionated console tool for PVE 8 with SolidFire written in PowerShell 7 (Linux, Windows) - can be found [here](https://github.com/scaleoutsean/firemox). Likely to work with PVE 9.1
- Read [this](https://scaleoutsean.github.io/2025/06/24/initial-exploration-solidfire-proxmox-plugin.html) if interested in building SolidFire plugin for Proxmox
- Read considerations for filesystems with compression in post above; also [this post](https://scaleoutsean.github.io/2024/02/29/ubuntu-2404-lts-with-netapp-solidfire.html)
  - There's a post about ZFS with SolidFire on the same blog, it's for Ubuntu 24.04 but it applies to any iSCSI client with ZFS
  - QEMU/KVM virtualization
  - LXC containers
- Proxmox PVE 7.1 (Debian-based) [with SolidFire 12.3](https://scaleoutsean.github.io/2022/04/05/proxmox-solidfire.html)

#### Linux-related (OpenStack, KVM, Oracle VM)

- Juju Charms for SolidFire Cinder driver
  - [Official OpenStack](https://github.com/openstack/charm-cinder-solidfire)
  - [Personal](https://github.com/scaleoutsean/charm-cinder-solidfire) - built with software current in September 2025 (builds cleanly but not tested)
- NetApp's [OpenStack resources and docs](https://netapp-openstack-dev.github.io/openstack-docs/draft/cinder/configuration/cinder_config_files/section_solidfire-conf.html) for SolidFire
- Cinder driver for OpenStack (in-tree, does not need to be installed, it only needs to be configured - see [this video](https://youtu.be/rW5ZTlyhm7U))
  - RHOSP16 certification: https://catalog.redhat.com/software/openstack/detail/2257111
  - Cinder Active-Active [enabled](https://docs.openstack.org/cinder/ussuri/reference/support-matrix.html#operation_active_active_ha)

- [Oracle VM](https://linux.oracle.com/pls/apex/f?p=117:3::::::) (look under Storage Systems > NetApp)
- Additional details about SolidFire in Linux environments: [solidfire-linux](https://github.com/scaleoutsean/solidfire-linux/)
- HashiCorp Nomad can schedule QEMU VMs on static SolidFire-backed volumes
- KVM users should provision disks with "Discard mode: unmap" to ensure rethinning of VM disks/volumes (`<driver name='qemu' type='qcow2' discard='unmap' />`) for OS that support TRIM/UNMAP

#### Oracle VirtualBox

- There are two ways known to me to use VirtualBox: one is as built by Oracle, another is [VirtualBox with KVM](https://github.com/cyberus-technology/virtualbox-kvm). The latter approach is newer and needs investigation
- VirtualBox's iSCSI initiator isn't officially supported but [it appears to work](https://youtu.be/EqxK-mT9Fxw) on both Linux and Windows (VirtualBox (host) iSCSI initiator for Windows seems prone to timeouts and I/O errors; it's better to use Linux or Windows initiators out of guest VMs)
- VirtualBox on top of OS-provisioned storage works as usual, as do supported VirtualBox guests with direct access to SolidFire iSCSI targets
- VirtualBox with KVM is a to-do item and 

#### Virtual Desktop Infrastructure and End User Computing (VDI & EUC)

- [VMware EUC/VDI with VMware Horizon View](https://docs.netapp.com/us-en/hci-solutions/nhci_euc_vmware.html)
- [Citrix Virtual Desktop and Virtual Apps](https://docs.netapp.com/us-en/hci-solutions/citrix_executive_summary.html)
- [Hybrid Cloud VDI with NetApp Virtual Desktop Service](https://docs.netapp.com/us-en/hci-solutions/hcvdivds_netapp_virtual_desktop_service_overview.html) - works with NetApp Global File Cache (GFC) for SMB

### Kubernetes and Containers

#### Get started with SolidFire

- Download and deploy SolidFire Demo VM (look for Element Demo VM or SolidFire Demo VM on this page). Estimated time: 30 min to download, 30 minutes to setup the first time you try
- To start using SolidFire from Kubernetes, head to my SolidFire-focused micro-site [Kubernetes with SolidFire](https://solidfire-kubernetes.pages.dev/) for a set of SolidFire-focused configuration steps. Estimated time: 15 minutes

#### CSI Provisioners

- [NetApp Astra Trident](https://github.com/NetApp/trident) - CSI-compatible dynamic volume provisioner for container platforms (Docker, Kubernetes, Red Hat OpenShift, Rancher RKE and others)
- OpenStack users may be able to [use SolidFire with Cinder CSI Plugin for Kubernetes](https://github.com/kubernetes/cloud-provider-openstack/blob/master/docs/cinder-csi-plugin/using-cinder-csi-plugin.md) - a demo and notes can be found [here](https://scaleoutsean.github.io/2022/03/02/openstack-solidfire-part-2.html)

#### SolidFire Operator for Kubernetes

- It hasn't been built, but it can be built. One such attempt can be found [here](https://github.com/scaleoutsean/solidfire-operator)
- It is recommended to use it to automate configuration of things SolidFire that Trident CSI doesn't touch

#### Red Hat OpenShift Container Platform

- You can run it two ways: VM-based OCP VMs on vSphere, Red Hat Virtualization or OpenStack, and bare metal-based OCP on RHEL. See the [official solution page](https://docs.netapp.com/us-en/netapp-solutions/containers/rh-os-n_solution_overview.html#netapp-trident) for additional details

#### Rancher

- Rancher on NetApp HCI: just configure it with Trident CSI. See the official NetApp HCI solutions page for additional details. In late 2020 I created a personal micro-site with notes on this solution from a NetApp HCI and SolidFire angle [here](https://scaleoutsean.github.io/solid-rancher), but I no longer maintain it because NetApp HCI is no longer sold, so maybe also check this newer SolidFire-focused micro-site [Kubernetes with SolidFire](https://solidfire-kubernetes.pages.dev/) instead.
- Provision Rancher K8s to NetApp HCI vSphere clusters from the CLI with [ez-rancher](https://github.com/NetApp/ez-rancher/)

#### Flatcar Container Linux

- Flatcar Container Linux notes can be found [here](https://scaleoutsean.github.io/2021/12/07/flatcar-linux-with-solidfire-iscsi.html). CoreOS users may find them useful, too

#### Google Anthos

- Anthos with Trident CSI is supported on vSphere clusters. See the official NetApp HCI solutions page for additional details

#### Docker CE and Mirantis Kubernetes Engine (MKE)

- Docker and other [container orchestrators supported](https://netapp-trident.readthedocs.io/en/latest/support/requirements.html#supported-frontends-orchestrators) by NetApp Trident CSI
- Docker Swarm is not supported with SolidFire and Trident, but Mirantis Kubernetes Engine is. More on Mirantis MKE with SolidFire can be found [here](https://scaleoutsean.github.io/2021/05/02/mirantis-mke-netapp-trident-solidfire)

#### Platform9 Managed Kubernetes (PMK)

- See [here](https://scaleoutsean.github.io/2022/03/31/platform-managed-kubernetes-pmk-on-prem-solidfire.html) with Trident v22.01, for example

#### VMware Photon 4.0

- Photon comes with iSCSI SRPMs which can be built and made to [work with SolidFire](https://scaleoutsean.github.io/2022/03/11/vmware-photon-iscsi-solidfire.html)

#### KubeVirt (and OCPv)

- KubeVirt v0.59 isn't easy to use, but it works with SolidFire 12 and Trident v23.01, [see here](https://scaleoutsean.github.io/2023/02/12/backup-restore-kubevirt-vms-with-solidfire-kasten-kubernetes.html). Interestingly, it appears that regular SolidFire PVCs appear as block devices when attached to KubeVirt VMs (in theory one should use Block mode, but that doesn't appear necessary)
- OCPv uses Trident, so non-ONTAP-specific Trident features should work the same as they do with KubeVirt

#### HashiCorp Nomad 

- Nomad can schedule services with Docker using static host volumes backed by SolidFire. I also got it to work with Trident Docker Volume Plugin. If the VM gets its HA from hypervisor, this may be a way to get HA for these Docker workloads. See [this](https://scaleoutsean.github.io/2022/03/23/nomad-solidfire-hostpath-volumes.html) for additional details
- LXC-style containers may be able to work on host volumes (static provisioning) as well
- Trident CSI is unlikely to work with Nomad CSI, but Cinder CSI might (needs testing)

### File-sharing (NFS, SMB)

- SolidFire itself is iSCSI only, so for file sharing you'd need another layer (VM or appliance) to consume iSCSI and share it with SMB or NFS or S3 clients
- Example 1: NetApp ONTAP Select 9.10 - single node or HA, including Active-Active stretch clusters with one ONTAP Select VM and NetApp HCI cluster per each site ([Metrocluster SDS](https://docs.netapp.com/us-en/ontap-select/concept_ha_config.html))
  - Read-only and read-write caching:
    - NFS (on-prem and hybrid cloud, read-only): NetApp ONTAP Select with [FlexCache](https://www.netapp.com/us/info/what-is-flex-cache.aspx)
    - SMB (hybrid cloud, read-write):
      - NetApp FlexCache (ONTAP Select 9.8+)
      - [NetApp Global File Cache](https://cloud.netapp.com/global-file-cache) running as edge node in Microsoft Windows VM, with core file service running in public cloud (Cloud Volumes ONTAP or Cloud Volumes Service). As indicated, you don't need ONTAP Select on NetApp HCI for this one
    - S3 - use ONTAP S3; this is recommended for small object stores (container registry, source code, etc.), use something like StorageGRID for large data and pre-compressed content (videos, compressed logs)
- Example 2: any modern OS with NFS, SMB or S3 service

### CLI, API, SDK Resources

#### API

- SolidFire has versioned API which means you can run your "old" automation scripts against an older API endpoint of your choosing (e.g. API endpoint version 8.0 is still available and works (as of 12.2) despite SolidFire 8 no longer being supported)
- SolidFire / Element Software API Reference Guide:
  - HTML: [v12.3](https://docs.netapp.com/us-en/element-software/api/index.html)

#### API Gateways

- SolidFire WAC Gateway - a non-trivial proof-of-concept API gateway for ASP.NET and IIS
  - It can be used for improved RBAC/ABAC. See [this](https://scaleoutsean.github.io/2025/07/26/solidfire-windows-admin-center-gateway.html) and [this](https://scaleoutsean.github.io/2025/07/30/solidfire-windows-admin-center-extension.html) post

#### CLI

- SolidFire has two CLIs - PowerShell & Python (not really maintained, but good (better!) CLIs are now very easy to build with Python)
- Python CLI: `pip3 install solidfire-cli` (but better build your own)
- PowerShell: `Install-Module SolidFire.Core` (PS 7 on x64; `SolidFire.Core` has been field-tested and found to work on ARM64, including Linux up to PS 7.4)
  - For PowerShell 7.5 and higher you probably have to [drop the Tools](https://scaleoutsean.github.io/2025/06/29/solidfire-with-powershell-7.html) and fall back to Invoke-RestMethod
  - Another, unofficial option is to write own CLI or use a CLI that works with a SolidFire API gateways (see "API Gateways" above)

#### SolidFire/Element Software Development Kits (SDKs)

- Releases:
  - [SolidFire Python SDK](https://github.com/solidfire/solidfire-sdk-python) (`pip3 install solidfire-sdk-python`)
  - [SolidFire Microsoft .NET SDK](https://github.com/solidfire/sdk-dotnet)
  - [SolidFire Java SDK](https://github.com/solidfire/solidfire-sdk-java)
  - [SolidFire Ruby SDK](https://github.com/solidfire/solidfire-sdk-ruby)
  - [(Unofficial) SolidFire Go SDK](https://github.com/solidfire/solidfire-sdk-golang) and its cousin [solidfire-go](https://github.com/j-griffith/solidfire-go) with a convenient wrapper for common volume operations.

### Automation

- Postman JSON [collection](https://github.com/solidfire/postman) for Element software

#### Model Context Protocol

- [MCP](https://modelcontextprotocol.io/introduction) lets you develop MCP for SolidFire in minutes using [Python](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file). [This blog post](https://scaleoutsean.github.io/2025/05/20/get-started-with-netapp-solidfire-mcp-server.html) has a simple example

#### Automation and Configuration Tools and Frameworks

- [community.solidfire](https://github.com/scaleoutsean/netapp.solidfire/) is my salvage-fork of NetApp abandonware `netapp.elementsw` - probably your best shot at getting something done with Ansible Core 2.20. Has some improvements the community has asked for years ago.
  - [netapp.elementsw](https://galaxy.ansible.com/netapp/elementsw?extIdCarryOver=true&sc_cid=701f2000001OH7YAAW) formerly usable collection for Element Software (`ansible-galaxy collection install netapp.elementsw`). Here's the [Github archive](https://github.com/ansible-collections/netapp.elementsw), in case you want to fork it
- [SolidFire Puppet plugin](https://github.com/solidfire/solidfire-puppet), unlikely to be usable
- My experimental provider with support for Terraform 1.5.7 can be found [here](https://github.com/scaleoutsean/terraform-provider-solidfire). Supports the same things as the official version plus some extras (in different stages of completeness): QoS, cluster pairing and volume replication 
  - A "community" provider which community never provided for, [Terraform Provider for NetApp Element Software](https://github.com/NetApp/terraform-provider-netapp-elementsw), is now outdated. It supported resources IQN, VAG, account, volume (find working examples in the repo's examples directory). You may try to install it directly from [Terraform registry](https://registry.terraform.io/providers/NetApp/netapp-elementsw/latest) but it's unlikely to work with modern Terraform
  
- Any application or tool that can consume JSON-RPC or one of SolidFire CLIs or SDKs can be used to automate. Fringe examples: backup SolidFire to S3 with [Kestra](https://scaleoutsean.github.io/2022/03/22/solidfire-storagegrid-data-workflows-kestra.html), [PowerShell in .NET notebook](https://scaleoutsean.github.io/2022/03/29/manage-solidfire-jupyter-powershell.html)

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
- Monitor performance and OpEx of all on-prem assets (NetApp- and non-NetApp-made) as well as in public clouds (find examples in NetApp [WP-7319](https://www.netapp.com/us/media/wp-7319.pdf))

#### VMware / Blue Medora True Visibility for VMware vRealize Operations

- True Visibility [product suite](https://bluemedora.com/products/vmware-vrealize-true-visibility/) (now part of VMware)
- See True Visibility for NetApp HCI and SolidFire [product documentation](https://support.bluemedora.com/s/article/User-Documentation-vRealize-Operations-Management-Pack-for-NetApp-HCI-SolidFire)

#### VMware vRealize Log Insight

- Log Insight [can serve (v8.1)](https://docs.vmware.com/en/vRealize-Log-Insight/8.1/com.vmware.log-insight.administration.doc/GUID-848E4804-3837-4D5E-956E-2216B17376AD.html) as destination for SolidFire logs

#### Graylog

- Redirect SolidFire log directly or indirectly (for example first to syslog-ng and from there forward to Graylog in the GELF format)
- For structured search see the Logstash how-to linked below, maybe it will help you

#### Elasticsearch (ELK stack)

- Redirect SolidFire log to syslog-ng or LogStash or whatever, and from there to Elastic
- A how-to article for Filebeat/Logstash as well as SolidFire API-based queries can be found [here](https://scaleoutsean.github.io/2021/10/18/solidfire-syslog-filebeat-logstash-elk-stack.html)
- Elasticsearch 8 examples with SolidFire using Trident Docker Volume Plugin, Trident CSI, and Cinder CSI can be found [here](https://scaleoutsean.github.io/2022/03/06/elastic-elk-stack-on-netapp.html)

#### InfluxDB v3 - SolidFire Collector (SFC) v2

- [SolidFire Collector](https://github.com/scaleoutsean/sfc/) is a permissively-licensed monitoring and alerting for SolidFire and NetApp HCI storage
  - Formerly HCICollector, [completely rewritten and improved](https://scaleoutsean.github.io/2024/05/29/sfc-v2.html). There's a [14-minute video demo](https://rumble.com/v513sls-solidfire-collector-v2.html) which talks about the database, measurements, dashboarding and the improvements compared to HCI Collector v0.7
  - v2.1 uses latest & greatest InfluxDB 3 back-end with optional S3 tiering
  - Collects snapshot schedules and replication-related metrics (HCI Collector does not)
  - Requires valid TLS certificate on SolidFire MVIP, InfluxDB
  - Dockerfile available for DIY packaging in seconds

#### Graphite - HCI Collector v0.7.x

- Older version of [SolidFire Collector](https://github.com/scaleoutsean/sfc/tree/v0.7.2), not recommended for large clusters (use SFC v2)
- Uses Graphite back-end
- Dockerfile and Kubernetes templates available
- It should be easier to use Solidfire Exporter (below) and translate scrape Prometheus into Graphite or something like that

#### Prometheus - solidfire-exporter

- [SolidFire Exporter](https://github.com/mjavier2k/solidfire-exporter/) fetches and serves SolidFire metrics in Prometheus format
  - Recommended for SolidFire in Kubernetes environments

#### Telegraf

- You can use Telegraf exec input to gather SolidFire metrics via the API and send to InfluxDB
  - Or use file input to "harvest" output from SolidFire CLI commands 
  - There's a sample script that collects SolidFire volume properties and stats in the scripts directory. You can read about it [here](https://scaleoutsean.github.io/2024/05/20/netapp-solidfire-input-for-telegraf.html)
- Collect SNMP or other metrics with [Telegraf](https://scaleoutsean.github.io/2021/08/13/solidfire-snmp-v3-grafana.html)
  - SolidFire SNMP output is very basic, so if you need more details use exec input above to collect them, or use Prometheus exporter for SolidFire or SFC
  - PowerShell script that gathers volume metrics and outputs them in InfluxDB v1 line format can be found in the scripts directory (see Scripts, below)
- Telegraf supports InfluxDB input; see Scripts below for a simple PowerShell script that can output SolidFire volume metrics in the InfluxDB format for pick up by Telegraf

#### Prometheus - NetApp Trident metrics

- SolidFire
  - use SolidFire Exporter (above)
  - another options is SolidFire SNMP-to-Telegraf-to-Prometheus (example [configuration files](https://scaleoutsean.github.io/2021/08/13/solidfire-snmp-v3-grafana))
- NetApp Trident
  - In v20.01 NetApp Trident delivered support for Prometheus metrics. A how-to is available [here](https://netapp.io/2020/02/20/prometheus-and-trident/)
  - [Example](https://scaleoutsean.github.io/2021/05/25/external-access-to-netapp-trident-solidfire-metrics.html) for SolidFire

#### Icinga and Nagios

- [ElementOS-Monitoring](https://github.com/aleex42/elementOS-monitoring) - more [here](https://blog.krogloth.de/nagios-icinga-monitoring-for-netapp-solidfire/)
- [nagfire](https://github.com/scaleoutsean/nagfire/) - supports status check of both SolidFire clusters and individual nodes (Python 3)

#### SNMP and SolidFire MIBs

- SolidFire MIBs may be downloaded from the SolidFire/Element Web UI. You can download the MIB files and open them to see what events and stats are gathered and sent by it
- SolidFire OID is 1.3.6.1.4.1.38091 (`.iso.org.dod.internet.private.enterprises.solidFire`)
  - For v3, EngineID's are unique per node; find them with `snmpwalk -DALL -v3 -l AuthNoPriv -u netapp -a MD5 -A "NetApp123$" -x DES -X "NetApp123$" $MIP 2>&1 | grep "probe found engineID"` (h/t Mike Henry) or Wireshark dump of `snmpwalk -v3` against each MIP
- SNMP is disabled by default. If you enable it, you may choose v2 or v3
  - SNMP Traps are sent out as v2. If SNMP v3 is required, you can set up an SNMP v2 to v3 trap forwarder (see [here](https://github.com/scaleoutsean/solidtrapper); there are commercial products that can do this)
- Check SolidFire Postman collection for SNMP-related API methods (there's 10 or so of them). For example, `SnmpSendTestTraps` lets us send test SNMP Trap from MVIP once SNMP is enabled and configured
- Deep dive into SolidFire SNMP can be found [here](https://scaleoutsean.github.io/2021/07/19/solidfire-mib-snmp-monitoring)
- Telegraf SNMP plugin can be used to extract SolidFire SNMP data (see link to a how-to under Prometheus, above)

#### Splunk

There are several ways to integrate:

- Performance and status monitoring: use solidfire-exporter and [scrape Prometheus metrics from Splunk](https://www.splunk.com/en_us/blog/devops/metrics-from-prometheus-exporters-are-now-available-with-the-sfx-smart-agent.html?locale=en_us)
- Logs: redirect SolidFire cluster's syslog to Universal Forwarder
- Events and basic performance monitoring: use SNMP GETs and/or send SNMP traps to UF or Indexer. The SolidFire MIB files can be downloaded from the SolidFire Web UI.
- Follow this [high level post](https://scaleoutsean.github.io/2023/11/12/send-solidfire-metrics-splunk-hec-http-event-collector.html) to get you started with HEC (SolidFire metrics) and Universal Forwarder (SolidFire syslog)

#### Syslog Forwarding

- SolidFire (or NetApp HCI or eSDS)
  - Forwarding to external syslog target may be configured through the CLI or the API (see `SetRemoteLoggingHosts` method). Element uses TCP and the log may be forwarded to one or more destinations. Sample lines from the log are provided further below
  - VMware-based NetApp HCI surfaces Element storage cluster events and alerts to vCenter; if ActiveIQ is enabled, these alerts are also sent to ActiveIQ
- mNode and NetApp Hybrid Cloud Control (HCC)
  - There are two components: mNode logs (rsyslog) and HCC (Docker service, in the current version). Both can be configured to forward logs to external syslog target (TCP or UDP). Only the former can forward to multiple destinations.
  - `GET /logs` from HCC may be used to obtain the logs of individual HCC services (containers), which Docker service currently does not forward. This could be coded into a "polling" script written in PowerShell or Python, for example. See the HCC API for more on using this API method or [this](https://scaleoutsean.github.io/2020/12/08/get-bearer-token-for-netapp-hci-hybrid-cloud-control-logs.html) article.

#### Security and General Auditing

- Common Criteria evaluation for SolidFire 12.2 can be found [here](https://www.commoncriteriaportal.org/files/epfiles/550-LSS%20ST%20v1.0.pdf)
- White paper on [PCI DSS](https://www.coalfire.com/resources/white-papers/netapp-hci-verified-architecture-for-pci-dss) contains information for users with PCI DSS compliance requirements
- Log handling: see Syslog Forwarding above
  - Due to space constraints within SolidFire storage nodes and mNode, if longer log retention is required it is suggested to forward logs to external destination
- See [TR-4840](https://www.netapp.com/pdf.html?item=/media/19389-tr-4840.pdf) and SolidFire documentation for details on authentication and authorization (including MFA/2FA)
- See the KMIP notes in this repo for practical notes on TLS certificates and KMIP

#### ServiceNow integration

- See the [official integration](https://docs.servicenow.com/bundle/rome-it-operations-management/page/product/service-mapping/reference/solidfire-storage-pattern.html) by ServiceNow
- Another way, not proven but [looks doable](https://scaleoutsean.github.io/2021/12/14/integrate-solidfire-with-servicenow.html), is indirectly through Elasticsearch-ServiceNow integration
  - This would require SolidFire log redirection with structured logging and alerting in Elasticsearch (a recipe can be found [in this post](https://scaleoutsean.github.io/2021/10/18/solidfire-syslog-filebeat-logstash-elk-stack.html))
  - Alternatively, and especially if you're interested in making use of SNMP traps - see under SNMP for more - there's a ["mega post" on all things SolidFire SNMP](https://scaleoutsean.github.io/2021/07/19/solidfire-mib-snmp-monitoring.html) which shows how SolidFire events can be filtered and used to create alerts. SNMP Traps can be sent to Elastic with Telegraf SNMP Trap plugin. There's no detailed how-to for that, but there's a post for SolidFire SNMP with Telegraf [here](https://scaleoutsean.github.io/2021/08/13/solidfire-snmp-v3-grafana.html). You'd have to use a different plugin (SNMP Traps for Telegraf) or [Logstash SNMP Trap plugin](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-snmptrap.html) or something similar.

#### Zabbix

- For SolidFire faults (failed disk, loose cable, etc.), it's probably easiest to enable SNMP Traps. See SNMP-related SolidFire information on this page and check out my mega blog post on SOlidFire and SNMP
- For performance monitoring you can also use any of indirect methods. For example, use SolidFire Exporter to send metrics to Prometheus, and use Zabbix to scrape Prometheus. Similar approach can be used to monitor faults: redirect SolidFire syslog to Logstash or even Elasticsearch - Zabbix can work with both of these

#### Event Notifications

- Users with existing notification solution: use Syslog forwarding or SNMP (see deep dive linked from under SNMP & SolidFire MIBs above)
- You may also [integrate](https://youtu.be/aiwkKQaz7AQ) NetApp ActiveIQ with your existing monitoring application
  - NetApp ActiveIQ: mobile app notifications (faster), email notifications (slower; enable them in the ActiveIQ Web UI)
  - Grafana: [HCICollector](https://github.com/scaleoutsean/hcicollector) and (Grafana in general, for example with SolidFire Exporter) can send email and other notifications
  - Icinga and Nagios (email)
  - SolidFire syslog forwarding to ElasticSearch with support cases created in ServiceNow or other back-end
  - Grafana or [Prometheus](https://scaleoutsean.github.io/2021/08/13/solidfire-snmp-v3-grafana.html) or any other sink which can receive SolidFire log or SNMP traps
  - SolidFire-to-Slack could work the same way: watch SolidFire (or Elastic or ActiveIQ, etc.) for events, use a webhook to sent notifications to a Slack channel or user

### Replication, DR and BC (Site Failover)

#### Storage replication management with Longhorny, a SolidFire replication management tool (OSS)

- [Longhorny](https://github.com/scaleoutsean/longhorny) is a permissively licensed script for CLI-based replication management. It supports only 1-to-1 cluster and volume relationships. It may be used to pair/unpair clusters, pair/unpair volumes, change direction of replication, and more. Language: Python 3. There's a short [demo](https://rumble.com/v513r8w-project-longhorny.html) (5m11s) if you want to see the main features
- [Kubefire](https://github.com/scaleoutsean/kubefire) focuses on using Longhorny and other tools in Kubernetes environments with Trident CSI. Additional notes on Trident CSI can be found in Backup & Restore section. 
  - Storage cluster failover for one Kubernetes cluster with Trident CSI and two SolidFire clusters is one of two approaches described in Kubefire scenarios, although not the recommended one. It uses NetApp Trident's Volume Import feature (a quick demo (2m55s) can be viewed [here](https://youtu.be/aSFxlGoHgdA) while some additional content available on my blog. For two Kubernetes clusters, each with own SolidFire cluster, you'd simply set up replication between SolidFire clusters (use consistency groups and group snapshots where necessary) and push Trident PVC-to-PV mapping to the remote site where you'd swap PV from SolidFire Cluster A for PVs replicated from SolidFire Cluster B so that you can promote Cluster B's volume replicas to readWrite mode and run Trident volume import before you start Kubernetes on that site.

### Backup and Restore

#### Built-in backup to S3

- Not full-featured backup software (i.e. there's no catalog and deduplication), but good for bulk backup of smaller volumes. Works with StorageGRID, ONTAP S3, MinIO (SolidFire >=12.3), [Wasabi](https://scaleoutsean.github.io/2022/01/19/solidfire-backup-restore-wasabi-s3.html), [Backblaze](https://scaleoutsean.github.io/2023/09/02/solidfire-backup-to-s3-backblaze-b2.html) and other S3 storage (not with CloudFlare R2)
- See [this](https://scaleoutsean.github.io/2021/04/21/solidfire-backup-to-s3.html) post and others on that blog
- SolidFire snapshots support [KV attributes](https://scaleoutsean.github.io/2023/04/01/using-solidfire-snapshot-attributes.html) for advanced snapshot workflows. For example we can use snapshot attributes to tag S3 snapshot objects
- Automation scripts for PowerShell can be found in the scripts folder of this repo; catalog feature could be created by inserting metadata into a DB such as SQL Express or PostgreSQL, but it may be easier to simply log to Elasticsearch
- [This post](https://scaleoutsean.github.io/2023/08/30/monitoring-solidfire-clone-and-backup-jobs.html) is a summary of options for monitoring of backup and restore jobs for the built in backup feature
- Example of sending backup job metrics to [InfluxDB](https://scaleoutsean.github.io/2024/04/24/netapp-solidfire-monitor-backup-influx-grafana-11.html)

#### VM and Bare Metal workloads

- While you backup SolidFire data by backing up front-end VMs or application data, the following vendors (ordered alphabetically) can integrate with SolidFire API to make data protection and business continuity easier and better
  - Cleondris HCC
  - Commvault
  - Rubrik
  - Veeam BR ([NetApp Element Plug-In for Veeam Backup & Replication](https://www.veeam.com/kb4044))
- Open-source integrations for non-CSI environments (Borg, Duplicati, Restic, Borg, Kopia, etc.)
  - Snapshot, clone and mount SolidFire volumes, then use a backup utility to replicate clone to backup storage (E-Series, etc.) or S3 (NetApp StorageGRID, AWS S3, MinIO, Wasabi, etc.)
    - Video demo with [Duplicati](https://youtu.be/wP8nAgFo8og)
    - An implementation with Restic written in PowerShell can be found in my [SolidBackup repository](https://www.github.com/scaleoutsean/solidbackup); with extremely simple modifications I was able to [apply the concept to backup SolidFire clones to Minio](https://scaleoutsean.github.io/2021/06/18/solidbackup-with-alternative-backup-clients)
    - [SimpleBackups](https://simplebackups.com/server-backup/) can be used to backup cloned & mounted volumes from a SolidBackup server
  - Kubernetes users can use Velero, VolSync and such (see below)
- You can also replicate volumes to, and then backup replicas from, ONTAP which becomes attractive with large backup jobs: set up SolidFire SnapMirror to ONTAP and backup the destination volume on ONTAP. When you have to backup a 20TB database on HCI, you're better off backing it up with NetApp HCI replicated to ONTAP than directly from HCI (either NetApp or any other)
- DR for Virtual Infrastructure
  - Native Synchronous and Asynchronous Replication - see NetApp TR-4741 or newer
  - Site failover
    - SolidFire SRA for VMware SRM
    - Some of the backup offerings mentioned above provide functionality similar to VMware SRM

#### Trident CSI with `solidfire-san` back-end

- Whatever non-standard stuff you want to do, having a mapping of Kubernetes-to-Trident-to-SolidFire could be nice to have! There's a script in the scripts folder, and a post about that [here](https://scaleoutsean.github.io/2024/06/01/pvc-volume-relationships-in-solidfire-trident-part-1.html)
- Can be backed up by creating thin clones and presenting them to a VM or container running a backup software agent (example with [Duplicacy](https://youtu.be/bvI7pgXKh6w))
- Enterprise backup software can also backup Trident volumes. Examples in alphabetical order:
  - Cloud Casa: use it with Velero engine with or without CSI plugin. CloudCasa was formerly exclusively hosted, but since Nov 2023 supports self-hosted deployments.
  - Commvault B&R: [documentation](https://documentation.commvault.com/11.21/essential/123637_system_requirements_for_kubernetes.html) and [demo](https://www.youtube.com/watch?v=kiMf9Fkhxd8). Metallic VM is another offering with this technology.
  - Kasten K10: [documentation](https://docs.kasten.io/latest/install/storage.html?highlight=netapp#netapp-trident) and [demo](https://www.youtube.com/watch?v=ShrSDwzQ0uU). 
  - Velero: [documentation](https://github.com/vmware-tanzu/velero) and [demo](https://www.youtube.com/watch?v=6RrlK2rmk24). It can work both [with](https://github.com/vmware-tanzu/velero-plugin-for-csi) and [without](https://scaleoutsean.github.io/2021/02/02/use-velero-with-netapp-storagegrid.html) Trident CSI. CSI support works and [CSI Snapshot Data Movement](https://scaleoutsean.github.io/2023/09/15/velero-csi-snapshot-data-movement-with-netapp-solidfire.html) (Velero v1.12) works as well! CloudCasa added support for Velero in April 2023. It appears [it can work](https://scaleoutsean.github.io/2023/04/15/cloudcasa-netapp-trident-solidfire.html) with Velero, Trident and SolidFire, but further testing is necessary
  - VolSync: consider [VolSync](https://scaleoutsean.github.io/2023/02/13/volume-replication-solidfire-kubernetes-volsync.html) when you need to backup to S3 or async-replicate SolidFire PVs to another Kubernetes cluster of any storage (e.g. E-Series with TopoLVM)
- PVCs used by KubeVirt VMs backed by SolidFire can be backed up and restored as any other Kubernetes PVCs, see [here](https://scaleoutsean.github.io/2023/02/12/backup-restore-kubevirt-vms-with-solidfire-kasten-kubernetes.html)
- Cinder CSI with SolidFire Cinder driver
  - See [this post](https://scaleoutsean.github.io/2022/03/02/openstack-solidfire-part-2.html) on how to deploy Cinder CSI with Openstack & SolidFire Cinder driver
  - Velero has a OpenStack Cinder driver [plugin](https://github.com/Lirt/velero-plugin-for-openstack) which I haven't tested
  - VM-level and native Kubernetes backup (Velero with an OpenStack plugin, etc.) wasn't tested, but crash-consistent Cinder snapshots from outside of Kubernetes work as usual
- E/EF-Series (with iSCSI host interface) attached to NetApp HCI is ideal fast Tier 1 backup pool/storage (gigabytes per second). You can find indicators of backup and restore performance in [this blog post](https://scaleoutsean.github.io/2020/12/30/netapp-hci-ef280-diskspd-for-backup)
  - Can act as replication target for Kubernetes environments with SolidFire. Consider evaluating [VolSync](https://scaleoutsean.github.io/2023/02/13/volume-replication-solidfire-kubernetes-volsync.html) for this
- Pre- and post-snapshot hooks for application-aware snapshots (backups): I've tested Kanister's (used by Kasten) as stand-alone and also from K10 and [NetApp Verda](https://scaleoutsean.github.io/2024/03/23/velero-netapp-verda-scripts-and-trident.html). These should work fine with Trident CSI.

### Security

- Minimal security footprint - HTTPS (management interfaces) and iSCSI (storage) and on-demand SSH for remote support
- Multi-Factor Authentication (MFA) for management access (since v12.0)

### Encryption

- Uses SED drives with cluster-managed keys
- Supports KMIP-compatible external key managers (see the IMT for the current list of tested ISV solutions (HyTrust, [Thales SafeNet KeySecure](./encryption/kmip-thales-keysecure.md), etc.))
- FIPS 140-2 
  - Element version >=12.5 - NetApp SolidFire H610S with [NCSM](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4297); until 2026
  - Element version <12.5 - NetApp HCI H610S-2F model only

#### Post-Quantum Cryptography

- This seems unlikely to happy in the product at this point, but there are alternatives:
  - [PQ API proxy](https://scaleoutsean.github.io/2025/10/10/post-quantum-crypto-proxy-for-solidfire-eseries-api.html) - inject a trusted proxy in between API clients and SolidFire. Commercial and OSS options are available - see the post for more
  - WAC Gateway - Windows .NET application server-based authorization and authentication with RBAC - see under API gateways. Rebuilt with .NET 9, this gives you PQC protection as well

## Demo VM, Tools and Utilities

### SolidFire/Element Demo VM

- Element Demo VM (SolidFire Demo VM): partners and customers may [download](https://docs.netapp.com/us-en/element-software/try/task_use_demonode.html) (NetApp partner or support login required) and use it at no cost. Data and configuration persist after a reboot. It works with Kubernetes (Trident), VMware ESXi and other iSCSI clients supported by SolidFire.
  - SolidFire Demo VM can't be upgraded and scaled out, but if you want to keep its data you can stand up another one, set up async replication to a new instance and remove the old instance once replication is done (that would require changes in Target on iSCSI nodes, if any, or import of new volumes with Trident)
  - VMware users can simply Storage vMotion their data. I tend to Storage vMotion data to another DS (not new SolidFire Demo VM), remove SolidFire VCP plugin from vCenter, remove Demo VM's iSCSI devices from any clients, delete the old Demo VM and deploy new VM in its place. Then I redeploy VCP (and register Demo VM in HCC, if I use it). The reason for doing things this way is I want to retain the same Storage and Management IP (which isn't easy to do if you use SolidFire replication to copy data from old to new Demo VM).
- NetApp OneCollect: this awesome and gratis multi-purpose utility that runs on Windows, Linux and in [Docker](https://hub.docker.com/r/netapp/onecollect/) containers is generally used for log data gathering but it can be used for configuration change tracking when set to run on schedule (watch [this video](https://www.youtube.com/watch?v=ksSs9wUi4sM) to get an idea - just don't run it on Element Management Node because that is not supported)

### Recorded Demos

- Videos created before 2022: [search YouTube for SolidFire](https://www.youtube.com/results?search_query=solidfire&sp=CAI%253D) and sort by most recent. Also check out [NetApp HCI](https://www.youtube.com/results?search_query=netapp+hci&sp=CAI%253D) video demos since NetApp HCI uses SolidFire storage
- Newer videos (2022 and later) are on [Rumble](https://rumble.com/search/video?q=solidfire)

## Scripts and How-To Articles

### Generic

Find them in the `scripts` directory in this repo:

- `Set-SFQosException` - set "temporary" Storage Policy on a SolidFire volume
  - When Storage QoS Policy ID is passed to this cmdlet, it takes Volume's current Storage QoS Policy ID value, stores it in Volume Attributes, and sets Volume to user-provided "temporary" Storage QoS Policy ID
  - If Storage QoS Policy ID is not provided, "reset" option resets Volume QoS to (original) value we stored in Volume Attributes before we applied exceptional QoS settings
  - Can be used for any task that can benefit from short-lived change in volume performance settings, such as backups (e.g. could be a hook for clone volume in Velero CSI Snapshot Data Movement)
  - Written with SolidFire PowerShell Tools 1.6 and PowerShell 7 on Linux, but should work with PowerShell 6 or newer on Windows 10 or Windows Server 2016 or newer
- `Get-SFVolEff` - simple PowerShell script to list all volumes with storage efficiency below certain cut-off level (default: `2`, i.e. 2x)
- `Get-SFDiskInventory.ps1` - gathers disk and node IDs, chassis slot and disk serials and shows them in a table or optionally saves to a  CSV file
- `parallel-backup-to-s3` - SolidFire-native Backup to S3
  - v1: runs `$p` parallel jobs to back up list of volumes identified by Volume ID (`$backup`) to an S3-compatible object store. The same script can be changed to restore in the same, parallel, fashion. Parallelization is over the entire cluster - the script is not aware of per-node job maximums so aggressive parallelization may result in backup jobs failing to get scheduled (but they can be resubmitted)
  - v2: executes up to `$p` parallel jobs *per each node*, where $p is an integer between 0 and the maximum number of bulk jobs per node (8). It's made possible by `sfvid2nid` (below). You can read more about it [here](https://scaleoutsean.github.io/2021/06/22/solidfire-backup-and-cloning-with-per-storage-node-queues.html)
- `sfvid2nid.py` - SolidFire volume ID to node ID mapping script (PowerShell). This information can be used to drive the maximum per-node number of bulk volume jobs (such as built-in backup) and sync jobs (such as copy and clone volume jobs)
- `hcc-hybrid-cloud-control-get-assets.ps1` - use PowerShell to connect to the NetApp Hybrid Cloud Control (HCC) API to get list of compute (ESXi) nodes. With that you can use PowerCLI to do VMware-related operations. More [here](https://scaleoutsean.github.io/2021/12/21/netapp-solidfire-hci-hcc-powershell.html).
- `disk-to-slot-to-node-assignment.py` - simple example of how to use SolidFire Python SDK to get disk-to-slot-to-node mapping from SolidFire
- `ansible_getting_started_with_solidfire.yml` - basic example for Ansible and SolidFire - creates a volume, changes its size and QoS properties, gets its details via the SolidFire API and then deletes/purges it
- `Manage-SolidFire.ipynb` - .NET notebook with simple examples for interactive SolidFire management in Jupyter
- `solidfire-capacity-report.ps1` - PowerShell-driven capacity and efficiency report script - creates single page HTML5 cluster capacity and efficiency report (you may view a sample HTML file to see what it does)
- `solidfire-telegraf-sample.ps1` - not meant for comprehensive use, but more for reference on using PowerShell to save SolidFire metrics to files formatted for InfluxDB import (meant to be picked by Telegraf or otherwise pushed out to InfluxDB v1)
- `kubernetes-trident-solidfire-pvc-to-volume-mapping.py` - map Kubernetes PVCs to NetApp Trident and SolidFire volume IDs (Python)
- `solidfire-qos-policy-id-to-trident-qos.py in scripts directory` - script sucks out one or more SolidFire QoS Policy IDs and spits them out as Trident Types, ready to copy-paste into your Trident configuration file for `solidfire-san`. Also spits out sample Storage Classes based on the values and policy names. See more [here](https://scaleoutsean.github.io/2024/06/19/trident-policy-sucker-for-solidfire-backends.html).

Some volume-cloning and backup-to-S3 scripts related to my SolidBackup concept can be found in the [SolidBackup repository](https://www.github.com/scaleoutsean/solidbackup).

### VMware

- SolidFire device names start with 6f47acc1 (vendor-specific identifier) while the NAA identifier is `naa.36f47acc1`
- PowerShell [script](https://github.com/kpapreck/test-plan/blob/master/kp-clone-snap-to-datastore.ps1) to clone a VMFS 6 volume from a SolidFire snapshot and import it to vCenter
- PowerShell [examples](https://github.com/solidfire/PowerShell/tree/release/1.5.1/VMware) for VMware. Do not use old performance-tuning scripts from the SolidFire PowerShell repo. They were written for ESXi 5.5 and 6.0. ESXi 6.5 and later have appropriate SolidFire MPIO settings built-in and require no special modification or tuning

### Windows

- PowerShell [scripts for Hyper-V 2012 R2](https://github.com/solidfire/PowerShell/tree/master/Microsoft) (need a refresh for Windows Server 2016+)
- See the [SolidFire Windows](https://github.com/scaleoutsean/solidfire-windows) repo for some newer PowerShell scripts specific to SolidFire with Windows

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

#### Date and Time Format in SolidFire API Responses

- The SolidFire and mNode API returns timestamp value in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) datetime format with extended UTC time (no TZ offset, etc.)
  - Sample: `{'timestamp': '2021-12-31T05:24:54Z'}`
  - Python 3: `print((datetime.datetime.utcnow()).strftime('%Y-%m-%dT%H:%M:%S%z')+"Z")` `->` `2021-12-31T05:27:33Z`
  - PowerShell 7: `Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ" -AsUTC` `->` `2021-12-31T05:27:01Z`
- The containers inside of HCC are another story - it depends on service. Some examples can be found [here](https://scaleoutsean.github.io/2020/12/08/get-bearer-token-for-netapp-hci-hybrid-cloud-control-logs.html)

#### Miscallenea

- [The shocking truth about SolidFire ModifySchedule method](https://scaleoutsean.github.io/2025/07/09/the-shocking-truth-about-createschedule.html)

## Questions and Answers

### Meta

Q: Is information on this page correct, up-to-date and endorsed by NetApp?

A: Absolutely not. For official information please visit the NetApp Web sites (such as www.netapp.com and www.netapp.io)

Q: I have a quick question about ...

A: Please visit the [NetApp Community Forum](https://community.netapp.com/t5/SolidFire-and-HCI/bd-p/solidfire_hci) and ask your question there.

### SolidFire / Element Demo VM

Q: Is Element Demo VM a simulator?

A: No. It's a fully functional single-node SolidFire cluster. Due to the fact that it's a VM that runs on modest hardware resources, it has some limitations (no encryption, etc) which are documented at the download page. It is not supported for production.

Q: I can't find SolidFire Demo VM 12.7, why?

A: It's unlikely it will be released. It seems 12.5 is the last release.

Q: Does Element Demo VM work on Virtualbox?

A: It's not supported, but version 12.3 works on Virtualbox 6.1 (find a demo on YouTube) on both Linux and Windows.

Q: Can Element Demo VM be used to estimate efficiency from compression and deduplication?

A: It does compress and deduplicate, but I haven't compared how it fares against physical SolidFire clusters.

Q: Can I throw couple of VMs on an Element Demo VM datastore to estimate how much I could save?

A: I believe that should be fairly accurate, but I haven't tested it. Get a representative sample of 5-10 VMs (up to 400GB combined) and clone them to an Element Demo VM-based test datastore. Give it a couple extra hours to churn through that data and take a look.

Q: Can I automate the provisioning of SolidFire Demo VM?

A: Absolutely. Provision it as any other OVA, then find the Management IP, and first configuration the node, and then create cluster. With DHCP on Management Network you may need to disconnect PowerShell Tools (or Python CLI/SDK) from the DHCP-assigned Management IP after you set static IP on the node, then reconnect to Static IP and configure your singleton cluster. You can also configure replicated clusters this way. With SSD backed hypervisors it takes about 10 minutes to setup two singleton clusters this way, or less if you clone VMs from a Demo VM template.

### Logging and Monitoring

Q: I'd like to do something with SoliFire logs, how do SolidFire logs look like?

A: The following lines were obtained by forwarding SolidFire cluster log to syslog-ng (from which we can forward it elsewhere): the second is an API call and therefore in JSON format). Element Software creates log using the rsyslog format (RFC-5424 and RFC-3164 (source: [Wikipedia](https://en.wikipedia.org/wiki/Rsyslog#Protocol)) and timestamps (format: `MMM  d HH:mm:ss`; RFC-3339). To make archived SolidFire logs more useful we'd have to create several filters (to gather only useful content and [convert it to a format that's easier to analyze](https://scaleoutsean.github.io/2021/10/18/solidfire-syslog-filebeat-logstash-elk-stack.html)) somewhere along log forwarding path. For comparison, vRealize Log Insight accepts formats in RFC-6587, RFC-5424, and RFC-3164 - see the Log Insight [link above](#vmware--blue-medora-true-visibility-for-vmware-vrealize-operations).

```shell
Jun  3 16:14:46 192.168.1.29 master-1[20395]: [APP-5] [API] 24018 DBCallback httpserver/RestAPIServer.cpp:408:operator()|Calling RestAPI::ListBulkVolumeJobs activeApiThreads=1 totalApiThreads=16 user=admin authMethod=Cluster sourceIP=192.168.1.12
Jun  3 16:14:46 192.168.1.29 master-1[20395]: {"action":"ApiCall","idg":"1775127282990285","idx":294566,"system":"Cluster","utc":"2020-06-03T16:14:46.058806Z","ver":"1.1","xClusterApiCall":{"AuthMthd":"Cluster","Method":"ListSyncJobs","SourceIP":"192.168.1.12","Threads":1,"Time":3,"TotalThreads":16,"Username":"admin"}}
```

The approach I took in the ELK post was to focus on ApiCall logs and use custom http_poller (see the post for more details). Timestamp inside of API responses is in ISO8601 extended UTC format (see other Q&A).

Q: How can I get mNode and HCC logs?

A: Simple answer: forward mNode VM syslog to external destination, and for HCC logs use the mNode API (although the latter can be done better in an unsupported way - see [here](https://scaleoutsean.github.io/2020/11/27/solidfire-mnode-hcc-log-forwarding.html)).

### Hypervisors and Containers

Q: What hypervisor platforms work with SolidFire iSCSI target?

A: To be clear, this is about iSCSI clients supported by SolidFire storage (which may or may not be different from hypervisors supported by NetApp HCI compute hardware). You can find the official NetApp info with the [NetApp Interoperability Matrix Tool (IMT)](https://mysupport.netapp.com/matrix/#welcome) (look under Element software, not NetApp HCI!). The simple answer is NetApp HCI ships with VMware, but SolidFire (that is, the iSCSI storage component of NetApp HCI) can work with other supported hypervisors (even at the same time). Some links to get you started with compatibility research:

- VMware ESXi - refer to the IMT
- Redhat OpenStack and Enterprise Virtualization - refer to the IMT
- MicroSoft Windows (Hyper-V) - search the WSC site (example for the [H615C](https://www.windowsservercatalog.com/item.aspx?idItem=4109a235-2b2e-3200-d3ef-065c8ea7c0c6&bCatID=1282))
- Citrix Hypervisor (formerly known as XenServer) - v8 is supported as per NetApp HCI VDI Solution with Citrix Hypervisor; for v7 refer to the HCLs for [storage](http://hcl.xenserver.org/storage/?vendor=56) and [servers](http://hcl.xenserver.org/servers/?vendor=56)
- Oracle VM - go [here](https://linux.oracle.com/pls/apex/f?p=117:3::::::). Click on Storage Systems and in filter rop-down list select NetApp. Look for SolidFire models from the NetApp HCI datasheet or Web site (for example, H610S)
- Other Linux distributions validated (Cinder iSCSI) for SolidFire Element OS - Ubuntu, SuSE, etc. (the details can be found in the NetApp IMT)
- Newer container-focused Linux distributions (Flatcar Container Linux, CoreOS) with iSCSI initiator
- Oracle Virtualbox - not suported (as it uses its own iSCSI client that isn't validated by NetApp) but it works and you may want to use it in a lab environment (it's not stable enough for production use)

What doesn't work so well is Virtualbox iSCSI client (unstable), and some microVMs OS (example: Firecracker) that have no iSCSI client those, however, could run on a hypervisor which connects to SolidFire and presents SolidFire volumes as block devices).

If unsure, contact NetApp with any questions or ask in the [NetApp Community Forum](https://community.netapp.com/t5/SolidFire-and-HCI/bd-p/solidfire_hci) (free membership account is required).

Q: Does SolidFire work with my Kubernetes?

A: If Trident works with it, SolidFire can too. Some K8s distributions known to work are listed in the Trident documentation, but other CSI-compatible distributions should work as well. I recommend to check out Trident [issues](https://github.com/NetApp/trident/issues) as well to see if there's anything that you care about. Note that issues and requirements change between releases, so sometimes you may be better off with an older release in which case you should check supported requirements for older Trident releases.

### Workloads

Q: Should I use SolidFire with (or for) ...

A: It depends. At the highest level of abstraction SolidFire is suitable for 95% of apps people virtualize or containerize on on-premises x86_64 infrastructure. If you think you're "one percenter", you may want to discuss your requirements with a NetApp SolidFire or Cloud Infrastructure architect. NetApp HCI may be able to accommodate even extreme workloads if data processing to external NFS or iSCSI storage such as NetApp AFF or E-Series (see [NVA-1152-DESIGN](https://www.netapp.com/pdf.html?item=/media/21016-nva-1152-design.pdf)). Some HCI vendors force such storage workloads on their HCI storage which doesn't work well (or sort-of-works, but at a much higher price).

Q: Is NetApp HCI suitable for AI, Splunk, Elasticsearch and similar "heavy" workloads?

A: For some applications from that stack (such as databases) it is, but for HDFS you may consider connecting compute nodes to ONTAP systems (usually NFSv3 or NFSv4) or E-Series (physical Raw Device Mapping (pRDM) to iSCSI, formatted with HDFS or [BeeGFS](https://blog.netapp.com/solution-support-for-beegfs-and-e-series/), for example.) [NVA-1152-DESIGN](https://www.netapp.com/pdf.html?item=/media/21016-nva-1152-design.pdf) shows how adding the smallest EF-Series model can add 5 GB/s of throughput to NetApp HCI clusters without any investment in FC switches or new HCI compute nodes.

  - [This post](https://scaleoutsean.github.io/2020/12/31/beegfs-on-netapp-hci-and-ef-series.html) demonstrates few GB/s with BeeGFS VMs (single HCI compute node attached to EF-Series EF280)
  - Performance guesstimates for [Splunk](https://scaleoutsean.github.io/2020/12/31/virtualized-splunk-on-netapp-hci-and-ef-series.html) and [Elasticsearch](https://scaleoutsean.github.io/2021/01/04/elasticsearch-on-netapp-h615c-ef280.html)

### Storage Services

Q: What protocols are supported?

A: For SolidFire, it's iSCSI for x86_64 Linux, Windows and VMware hosts. No UNIX and no Fibre Channel. See the next question for NFS and SMB.

Q: Okay, I want SolidFire but what about NFS and SMB?

A: You can buy a software-based ONTAP license (NetApp ONTAP Select) and run it off your ESXi or KVM compute node(s). It's great for small to medium file servers, DevOps, K8s integrations, and data that needs to be replicated to or from major public clouds (where you'd have NetApp Cloud Volumes ONTAP). For file servers with large amounts of data that cannot be compressed or deduplicated, Big Data, volumes that need extreme performance (GB/s), consider connecting your servers to an E-Series (iSCSI) or ONTAP (iSCSI, NFS v3/v4/v4.1) storage - even when such workloads can run on SolidFire, it's usually not a good choice (price/performance-wise).

ONTAP Select running on NetApp HCI compute nodes can store its data either (or both) on NetApp HCI storage or external storage supported by hypervisor (ESXi 6.7, for example).

- NetApp [TR-4669](https://www.netapp.com/us/media/tr-4669.pdf): HCI File Services Powered by ONTAP Select (vSphere 6 (older ONTAP 9) and 7 (newer ONTAP 9))
- NetApp ONTAP Select [documentation](https://docs.netapp.com/us-en/ontap-select/)

NetApp HCI users who got the free ONTAP Select with their system can also use S3 protocol with it, especially for small requests. [This post](https://scaleoutsean.github.io/2022/03/17/ontap-s3-performance-test.html) shows performance of a minimal OTS 9.10 on NetApp HCI Gen 1 hardware (H300 Series nodes).

### DevOps

Q: PowerShell Tools for SolidFire can't connect to SolidFire using PowerShell 7.4 or later. Why?

A: I assume .NET it was built against is too old. Unless they update it (I doubt they will), use native PowerShell code. Set request headers to contain Basic Authentication header and accept JSON and use those headers in all Invoke- requests. See [here](https://scaleoutsean.github.io/2025/06/29/solidfire-with-powershell-7.html) for an example.

Q: Where can I find some examples of SolidFire use in DevOps?

A: At this time (2025) it's best to read my blog and follow me on Github, really.

Q: When should I use the SolidFire API?

A: There are situations where certain operations may be done faster or more efficiently by talking directly to SolidFire API. Some examples:

- clone SolidFire volumes: automate, optimize or otherwise enhance your workflow
- set up replication relationships and/or failover procedures without having to rely on external integrations such as VMware SRM (SolidFire SRA)
- automate movement of data between VMware vRDM, Linux volumes and Docker containers
- speed up workflows by working directly with SolidFire API (Terraform plugin for SolidFire, SolidFire SDKs and CLIs)
- use an API method that's not (or not yet) exposed through a 3rd party integration (vCenter plugin) or even SolidFire SDK (for example, currently that is the case with Element storage Qos histograms)

Q: How can I use a feature that is available but not exposed in a SolidFire SDK or API or CLI?

A: PowerShell Tools for SolidFire and all SDKs have a wrapper method (Invoke SF API) that simplifies the use of the API methods for which there is no cmdlet or direct method in an SDK. You can also use generic JSON RPC calls which may be a good choice for simple scripts in which you don't intend to use a SolidFire SDK because you don't want to install additional dependencies for simple projects.

Q: How can I find the limits - say the maximum number of volumes - of my SolidFire cluster?

A: To get most if not all software-related limits use the API (`GetLimits`) or a CLI equivalent. For example, assuming `$MVIP` is the cluster management virtual IP, with SolidFire Powershell Tools `$sf = Connect-SFCluster $MVIP; $sf.limits` would do it. Note that there may be hardware-related limits or best practices that limit or impact overall cluster limits.

Q: Is there a quick way to try SolidFire PowerShell Tools or SolidFire Python CLI from Docker?

A: Yes. Sample Ubuntu-based container with SolidFire PowerShell Tools can be started with `docker run -it scaleoutsean/solidshell` (run `Connect-SFCluster` once inside). You can also build your own and include 3rd party PowerShell or Python modules you commonly use.

Q: Is there a way to implement RBAC for "tiered" storage provisioning (cluster admin - team - storage account)?

A: Yes, there are several ways. What's common to them all is you need something in between the API user and the SolidFire API point, which will intercept API calls and decide whether to let them through. The easiest is probably to use Ansible [like this](https://scaleoutsean.github.io/2022/02/14/middle-class-rbac-solidfire-ansible.html). If you dislike Ansible, you have two other choices: implement API reverse proxy that terminates TLS connections, dissects API calls and filters based on team membership, or build own API proxy application (which can be running behind an enterprise proxy) that does the same (accept JSON RPC calls, examine them against team membership stored in static files, Sqlite or DB service), and decide what to do with them. This [high-level recipe](https://scaleoutsean.github.io/2023/12/07/solidfire-rbac-for-json-rpc-api.html) shows how it can be done, but doesn't have the details of JSON-RPC dissection and analysis.

Q: How do I make the creation of clone volumes faster?

A: You probably can't, but in some workflows the following may help:
- If you need multiple clones, it may be faster to clone one volume to two, then two, four and eight in parallel. See [this](https://scaleoutsean.github.io/2023/08/30/monitoring-solidfire-clone-and-backup-jobs.html#faster-multiple-clones-from-a-single-volume)
- Depending on your use case, you may be able to pre-create clones and use them on-demand as explained in [this post](https://scaleoutsean.github.io/2023/11/22/genai-with-netapp-solidfire.html)

### iSCSI

Q: What is the WWN prefix for SolidFire devices?

A: Looks like `6f47acc10` to me (see `/dev/disk/by-id/wwn-0x` in this example output for a SolidFire block device):

```raw
    Id:                         by-id-scsi-1SolidFir6d6e347900000169f47acc0100000000
    IdLabel:                    
    IdType:                     ext4
    IdUUID:                     2f578565-ff3d-4566-9961-bfd0fb08dbe4
    IdUsage:                    filesystem
    IdVersion:                  1.0
    MDRaid:                     '/'
    MDRaidMember:               '/'
    PreferredDevice:            /dev/sdc
    ReadOnly:                   false
    Size:                       10000269312
    Symlinks:                   /dev/disk/by-id/scsi-1SolidFir6d6e347900000169f47acc0100000000
                                /dev/disk/by-id/scsi-26d6e347900000169f47acc0100000000
                                /dev/disk/by-id/scsi-36f47acc1000000006d6e347900000169
                                /dev/disk/by-id/scsi-SSolidFir_SSD_SAN_6d6e347900000169f47acc0100000000
                                /dev/disk/by-id/wwn-0x6f47acc1000000006d6e347900000169
                                /dev/disk/by-path/ip-192.168.103.30:3260-iscsi-iqn.2010-01.com.solidfire:mn4y.vol359.361-lun-0
                                /dev/disk/by-uuid/2f578565-ff3d-4566-9961-bfd0fb08dbe4
```
Example for iSCSI device `scsi-36f47acc1000000007868363700000063`:
  - `3` - NAA identifier
  - `6f47acc1` - SolidFire vendor-specific identifier
  - `0000000078683637` - hex SolidFire cluster ID (equivalent of `xh67` (ASCII), which appears in IQN for the target: `iqn.2010-01.com.solidfire:xh67.pve01.99`)
  - `00000063` - hex volume ID on SolidFire (volume ID 99 (decimal) in the SolidFire UI)

Q: Does SolidFire iSCSI support iSCSI reservations?

A: Yes.

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
