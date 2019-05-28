#!/usr/bin/env python
# -*- coding: utf-8 -*-

headers = {
            "Content-Type": "application/json, text/plain, */*",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0",
            "Accept-Encoding": "gzip, deflate"
        }

ACL_GET="/acl/get"
AGGREGATE_LIST="/aggregate/list"
AGGREGATE_NODE_DELETE="/aggregate/node/delete"
AGGREGATE_NODE_UPDATE="/aggregate/node/update"
AUTH_LOGIN="/auth/login"
AUTH_LOGOUT="/auth/logout"
AUTH_PROJECT_RESCOPE="/auth/project/rescope"
AUTH_TOKEN_VALIDATION_GET="/auth/token/validation/get"
BACKEND_DETAIL_LIST="/backend/detail/list"
BACKEND_DISABLE="/backend/disable"
BACKEND_DRIVER_GET="/backend/driver/get"
BACKEND_ENABLE="/backend/enable"
BACKEND_IMAGESUSAGE_GET="/backend/imagesusage/get"
BACKEND_IO_GET="/backend/io/get"
BACKEND_IO_LIST="/backend/io/list"
BACKEND_SNAPSUSAGE_GET="/backend/snapsusage/get"
BACKEND_TOTALUSAGE_GET="/backend/totalusage/get"
BACKEND_VOLSUSAGE_GET="/backend/volsusage/get"
CLOUD_RESOURCE_DETAIL_SHOW="/cloud/resource/detail/show"
CLOUD_RESOURCE_LIMIT_SHOW="/cloud/resource/limit/show"
CLOUD_RESOURCE_QUOTA_SHOW="/cloud/resource/quota/show"
CLOUD_RESOURCE_SUMMARY_SHOW="/cloud/resource/summary/show"
DRS_CONFIG_SHOW="/drs/config/show"
DRS_CONFIG_UPDATE="/drs/config/update"
DRS_HISTORY_SHOW="/drs/history/show"
DRS_SWITCH_UPDATE="/drs/switch/update"
FIREWALL_CREATE="/firewall/create"
FIREWALL_DELETE="/firewall/delete"
FIREWALL_LIST="/firewall/list"
FIREWALL_PROJECT_LIST="/firewall/project/list"
FIREWALL_SHOW="/firewall/show"
FIREWALLRULE_CREATE="/firewallrule/create"
FIREWALLRULE_DELETE="/firewallrule/delete"
FIREWALLRULE_LIST="/firewallrule/list"
FIREWALLRULE_SHOW="/firewallrule/show"
FLOATINGIP_ASSOCIATE="/floatingip/associate"
FLOATINGIP_CREATE="/floatingip/create"
FLOATINGIP_DELETE="/floatingip/delete"
FLOATINGIP_DISASSOCIATE="/floatingip/disassociate"
FLOATINGIP_LIST="/floatingip/list"
FLOATINGIP_SHOW="/floatingip/show"
HOSTMANAGER_ENABLE_UPDATE="/hostmanager/enable/update"
HOSTMANAGER_INFORMATION_GET="/hostmanager/information/get"
HYPERVISOR_CLUSTER_STATS_GET="/hypervisor/cluster/stats/get"
HYPERVISOR_DEVICE_PCI_LIST="/hypervisor/device/pci/list"
HYPERVISOR_DEVICE_USB_ATTACH="/hypervisor/device/usb/attach"
HYPERVISOR_DEVICE_USB_DETACH="/hypervisor/device/usb/detach"
HYPERVISOR_DEVICE_USB_LIST="/hypervisor/device/usb/list"
HYPERVISOR_HOST_LIST="/hypervisor/host/list"
HYPERVISOR_LIST="/hypervisor/list"
HYPERVISOR_STATS_LIST="/hypervisor/stats/list"
HYPERVISOR_VCPU_PINSET_GET="/hypervisor/vcpu/pinset/get"
IMAGE_CREATE="/image/create"
IMAGE_DELETE="/image/delete"
IMAGE_FILE_LIST="/image/file/list"
IMAGE_FILE_LOCATION_SHOW="/image/file/location/show"
IMAGE_FILE_LOCATION_UPDATE="/image/file/location/update"
IMAGE_LIST="/image/list"
IMAGE_SHOW="/image/show"
IMAGE_UPDATE="/image/update"
LBAAS_HEALTHMONITOR_CREATE="/lbaas/healthmonitor/create"
LBAAS_HEALTHMONITOR_DELETE="/lbaas/healthmonitor/delete"
LBAAS_HEALTHMONITOR_LIST="/lbaas/healthmonitor/list"
LBAAS_HEALTHMONITOR_SHOW="/lbaas/healthmonitor/show"
LBAAS_HEALTHMONITOR_UPDATE="/lbaas/healthmonitor/update"
LBAAS_LISTENER_CREATE="/lbaas/listener/create"
LBAAS_LISTENER_DELETE="/lbaas/listener/delete"
LBAAS_LISTENER_LIST="/lbaas/listener/list"
LBAAS_LISTENER_SHOW="/lbaas/listener/show"
LBAAS_LISTENER_UPDATE="/lbaas/listener/update"
LBAAS_LOADBALANCER_CREATE="/lbaas/loadbalancer/create"
LBAAS_LOADBALANCER_DELETE="/lbaas/loadbalancer/delete"
LBAAS_LOADBALANCER_LIST="/lbaas/loadbalancer/list"
LBAAS_LOADBALANCER_SHOW="/lbaas/loadbalancer/show"
LBAAS_LOADBALANCER_UPDATE="/lbaas/loadbalancer/update"
LBAAS_MEMBER_CREATE="/lbaas/member/create"
LBAAS_MEMBER_DELETE="/lbaas/member/delete"
LBAAS_MEMBER_LIST="/lbaas/member/list"
LBAAS_MEMBER_SHOW="/lbaas/member/show"
LBAAS_MEMBER_UPDATE="/lbaas/member/update"
LBAAS_POOL_CREATE="/lbaas/pool/create"
LBAAS_POOL_DELETE="/lbaas/pool/delete"
LBAAS_POOL_LIST="/lbaas/pool/list"
LBAAS_POOL_SHOW="/lbaas/pool/show"
LBAAS_POOL_UPDATE="/lbaas/pool/update"
LICENSE_ADD="/license/add"
LICENSE_ADDTEST="/license/addtest"
LICENSE_DEL="/license/del"
LICENSE_LIST="/license/list"
LOG_DOWNLOAD="/log/download"
LOG_OPERATION_LIST="/log/operation/list"
MAINTENANCE_CROSS_NODE_TASK_EXECUTE="/maintenance/cross/node/task/execute"
MAINTENANCE_NODE_STATE_CHECK="/maintenance/node/state/check"
MAINTENANCE_NODE_STATE_START="/maintenance/node/state/start"
MAINTENANCE_NODE_STATE_STOP="/maintenance/node/state/stop"
MAINTENANCE_NODES_CLOSE="/maintenance/nodes/close"
MAINTENANCE_NODES_START="/maintenance/nodes/start"
MAINTENANCE_SERVICE_LIST="/maintenance/service/list"
MAINTENANCE_SERVICE_RECOVERY="/maintenance/service/recovery"
MAINTENANCE_SERVICE_RESET="/maintenance/service/reset"
MAINTENANCE_STATE_GET="/maintenance/state/get"
MAINTENANCE_STATE_UPDATE="/maintenance/state/update"
MAINTENANCE_TMP_GET="/maintenance/tmp/get"
MAINTENANCE_TMP_UPDATE="/maintenance/tmp/update"
MONITOR_ALARM_EMAIL_SHOW="/monitor/alarm/email/show"
MONITOR_ALARM_EMAIL_UPDATE="/monitor/alarm/email/update"
MONITOR_ALARM_LEVEL_SHOW="/monitor/alarm/level/show"
MONITOR_ALARM_LEVEL_UPDATE="/monitor/alarm/level/update"
MONITOR_ALARM_LIMITS_UPDATE="/monitor/alarm/limits/update"
MONITOR_ALARM_RECORD_LIST="/monitor/alarm/record/list"
MONITOR_ALARM_SHOW="/monitor/alarm/show"
MONITOR_CLUSTER_INFOS="/monitor/cluster/infos"
MONITOR_CLUSTER_LIST="/monitor/cluster/list"
MONITOR_CLUSTER_OVS_SHOW="/monitor/cluster/ovs/show"
MONITOR_NODE_SHOW="/monitor/node/show"
MONITOR_PROJECT_SHOW="/monitor/project/show"
MONITOR_VM_ALARM_SHOW="/monitor/vm/alarm/show"
MONITOR_VM_LIST="/monitor/vm/list"
MONITOR_VM_SCREENSHOT_LIST="/monitor/vm/screenshot/list"
MONITOR_VM_SHOW="/monitor/vm/show"
NETWORK_BOND_CREATE="/network/bond/create"
NETWORK_BOND_DEL="/network/bond/del"
NETWORK_BOND_INTERFACE_ADD="/network/bond/interface/add"
NETWORK_BOND_INTERFACE_DEL="/network/bond/interface/del"
NETWORK_CREATE="/network/create"
NETWORK_DELETE="/network/delete"
NETWORK_EXTERNAL_CREATE="/network/external/create"
NETWORK_INTERFACE_ADD="/network/interface/add"
NETWORK_INTERFACE_DEL="/network/interface/del"
NETWORK_INTERFACE_INFORMATION_GET="/network/interface/information/get"
NETWORK_LIST="/network/list"
NETWORK_SHOW="/network/show"
NETWORK_TOPOLOGY_SHOW="/network/topology/show"
NETWORK_UPDATE="/network/update"
PORT_CREATE="/port/create"
PORT_DELETE="/port/delete"
PORT_LIST="/port/list"
PORT_SHOW="/port/show"
PORT_UPDATE="/port/update"
PROJECT_CREATE="/project/create"
PROJECT_DELETE="/project/delete"
PROJECT_LIST="/project/list"
PROJECT_RESOURCE_AVAILABLE_SHOW="/project/resource/available/show"
PROJECT_RESOURCE_QUOTA_SHOW="/project/resource/quota/show"
PROJECT_SHOW="/project/show"
PROJECT_UPDATE="/project/update"
PROJECT_USER_AVAILABLE_LIST="/project/user/available/list"
PROJECT_USER_GRANT="/project/user/grant"
PROJECT_USER_LIST="/project/user/list"
PROJECT_USER_REVOKE="/project/user/revoke"
PROJECT_VOLUME_AVAILABLE_SHOW="/project/volume/available/show"
ROUTER_CREATE="/router/create"
ROUTER_DELETE="/router/delete"
ROUTER_GATEWAY_ADD="/router/gateway/add"
ROUTER_GATEWAY_REMOVE="/router/gateway/remove"
ROUTER_INTERFACE_ADD="/router/interface/add"
ROUTER_INTERFACE_REMOVE="/router/interface/remove"
ROUTER_LIST="/router/list"
ROUTER_SHOW="/router/show"
ROUTER_UPDATE="/router/update"
SCHEDULER_CHECK_VM="/scheduler/check_vm"
SCHEDULER_CRON_ADD="/scheduler/cron/add"
SCHEDULER_CRON_DELETE="/scheduler/cron/delete"
SCHEDULER_CRON_LIST="/scheduler/cron/list"
SCHEDULER_CRON_SHOW="/scheduler/cron/show"
SCHEDULER_CRON_UPDATE="/scheduler/cron/update"
SCHEDULER_HISTORY_LIST="/scheduler/history/list"
SCHEDULER_REMOVE_SINGLE="/scheduler/remove_single"
SCHEDULER_TEST_ADD="/scheduler/test/add"
SCHEDULER_VOL_SNAP_ADD="/scheduler/vol/snap/add"
SNAPSHOT_CREATE="/snapshot/create"
SNAPSHOT_DELETE="/snapshot/delete"
SNAPSHOT_INSTANCE_ROLLBACK="/snapshot/instance/rollback"
SNAPSHOT_LIST="/snapshot/list"
SNAPSHOT_VOLUME_ROLLBACK="/snapshot/volume/rollback"
STATISTIC_NODES_LIST="/statistic/nodes/list"
STATISTIC_NODES_RECORDS_DOWNLOAD="/statistic/nodes/records/download"
STATISTIC_NODES_SHOW="/statistic/nodes/show"
STATISTIC_VM_RECORDS_DOWNLOAD="/statistic/vm/records/download"
STATISTIC_VM_SHOW="/statistic/vm/show"
STORAGE_CAPACITY_SHOW="/storage/capacity/show"
SUBNET_CREATE="/subnet/create"
SUBNET_DELETE="/subnet/delete"
SUBNET_IP_AVAILABLE_LIST="/subnet/ip/available/list"
SUBNET_LIST="/subnet/list"
SUBNET_SHOW="/subnet/show"
SUBNET_UPDATE="/subnet/update"
TIMEZONE_SHOW="/timezone/show"
USER_AVAILABLE_LIST="/user/available/list"
USER_CREATE="/user/create"
USER_DELETE="/user/delete"
USER_EXIST_SHOW="/user/exist/show"
USER_LIST="/user/list"
USER_PASSWORD_UPDATE="/user/password/update"
USER_PROFILE_UPDATE="/user/profile/update"
USER_PROJECT_SCOPE_LIST="/user/project/scope/list"
USER_ROLE_LIST="/user/role/list"
USER_SHOW="/user/show"
V2V_TASK_CANCEL="/v2v/task/cancel"
V2V_TASK_DELETE="/v2v/task/delete"
V2V_TASK_LIST="/v2v/task/list"
V2V_TASK_START="/v2v/task/start"
V2V_VMS_LIST="/v2v/vms/list"
VERSION="/version"
VM_AUTOSTART_SET="/vm/autostart/set"
VM_CLONE_CREATE="/vm/clone/create"
VM_CONSOLE_SHOW="/vm/console/show"
VM_CREATE="/vm/create"
VM_DELETE="/vm/delete"
VM_DRIVER_GET="/vm/driver/get"
VM_DRIVER_INSTALL="/vm/driver/install"
VM_DRIVER_UNCHECK="/vm/driver/uncheck"
VM_DRIVER_UNCHECK_LIST="/vm/driver/uncheck/list"
VM_DRIVER_UPDATE="/vm/driver/update"
VM_DRS_SET="/vm/drs/set"
VM_EXPORT="/vm/export"
VM_EXPORT_LOCATION_SHOW="/vm/export/location/show"
VM_EXPORT_LOCATION_UPDATE="/vm/export/location/update"
VM_LIST="/vm/list"
VM_MIGRATE="/vm/migrate"
VM_OWNER_CLEAR="/vm/owner/clear"
VM_OWNER_SET="/vm/owner/set"
VM_PAUSE="/vm/pause"
VM_PORT_ATTACH="/vm/port/attach"
VM_PORT_DETACH="/vm/port/detach"
VM_PORT_LIST="/vm/port/list"
VM_REBOOT="/vm/reboot"
VM_RESET="/vm/reset"
VM_RESIZE="/vm/resize"
VM_SECURITY_GROUP_SWITCH="/vm/security_group/switch"
VM_SECURITY_GROUP_UPDATE="/vm/security_group/update"
VM_SHOW="/vm/show"
VM_SNAPSHOT_CREATE="/vm/snapshot/create"
VM_SNAPSHOT_DELETE="/vm/snapshot/delete"
VM_SNAPSHOT_ROLLBACK="/vm/snapshot/rollback"
VM_SNAPSHOT_ROLLBACK_LIST="/vm/snapshot/rollback/list"
VM_START="/vm/start"
VM_STATS_SUMMARY_GET="/vm/stats/summary/get"
VM_STOP="/vm/stop"
VM_TEMPLATE_CREATE="/vm/template/create"
VM_TEMPLATE_DELETE="/vm/template/delete"
VM_UNPAUSE="/vm/unpause"
VM_UPDATE="/vm/update"
VM_VCPU_PIN_CLEAR="/vm/vcpu/pin/clear"
VM_VCPU_PIN_SET="/vm/vcpu/pin/set"
VM_VOLUME_ATTACH="/vm/volume/attach"
VM_VOLUME_DETACH="/vm/volume/detach"
VM_EXT_CONFIG_SHOW="/vm_ext/config/show"
VM_EXT_CONFIG_UPDATE="/vm_ext/config/update"
VM_EXT_PROJECT_DELETE="/vm_ext/project/delete"
VM_EXT_PROJECT_SHOW="/vm_ext/project/show"
VM_EXT_PROJECT_UPDATE="/vm_ext/project/update"
VM_EXT_PROJECTS_SHOW="/vm_ext/projects/show"
VM_EXT_QUOTA_UPDATE="/vm_ext/quota/update"
VM_EXT_VM_CONFIG_UPDATE="/vm_ext/vm/config/update"
VM_EXT_VM_DYN_SWITCH="/vm_ext/vm/dyn/switch"
VM_EXT_VM_MAN_START="/vm_ext/vm/man/start"
VM_EXT_VM_OFF="/vm_ext/vm/off"
VM_EXT_VM_ON="/vm_ext/vm/on"
VM_EXT_VM_SHOW="/vm_ext/vm/show"
VM_EXT_VM_STOP="/vm_ext/vm/stop"
VM_EXT_VMS_DELETE="/vm_ext/vms/delete"
VOLUME_ABNORMAL_LIST="/volume/abnormal/list"
VOLUME_CREATE="/volume/create"
VOLUME_DEFAULT_TYPE_LIST="/volume/default/type/list"
VOLUME_DELETE="/volume/delete"
VOLUME_EXTEND="/volume/extend"
VOLUME_LIST="/volume/list"
VOLUME_LIST3="/volume/list3"
VOLUME_RESET="/volume/reset"
VOLUME_SHOW="/volume/show"
VOLUME_TYPE_LIST="/volume/type/list"
VOLUME_UPDATE="/volume/update"