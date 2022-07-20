class Constants:


    # CONFIGURATIONID              = "configurationId"
    # APP                          = "app"
    # APPINTEGRATIONID             = "appIntegrationId"
    # MANAGEMENTPROFILEID          = "managementProfileId"
    # MESSAGEID                    = "messageId"
    # APPNAME                      = "appName"
    PAYLOAD                      = "payload"
    NATIVE_TYPE                  = "nativeType"
    RESOURCETYPE                 = "resourceType"
    RESOURCETYPES                = "resourceTypes"
    #
    #
    # CURRENT_RESOURCESET          = "currentResourceSet"
    # CURRENT_RELATIONSHIPSET      = "currentRelationshipSet"
    MONITOR_ID                    = "monitorId"
    # TEMPLATESHAVALUE             = "templateShaValue"
    # APPCONFIG                    = "appConfig"
    # APPCONFIGID                  = "appConfigId"
    # APPCONFIGSHAVAL              = "appConfigShaValue"
    #
    CREDENTIALS                  = "credentials"
    CREDENTIAL                   = "credential"
    FIELDNAME                    = "fieldName"
    CREDENTIALVALUE              = "credentialValue"
    CIPHER                       = "cipher"
    #
    DATA                         = "data"
    RESOURCES                    = "resources"
    RESOURCE_ID                   = "resourceId"
    # RESOURCESHAVALUE             = "resourceShaValue"
    # MONITORS                     = "monitors"
    # UUID                         = "uuid"
    METRICS                      = "metrics"
    # CONFIGURATIONNAME            = "configurationName"
    # ROOT_RESOURCE_TAGS           = "RootResourceTags"
    #
    MEMBER_OF                    = "memberof"
    # DEPENDENDS_ON                = "dependsOn"
    COMPONENT_OF                 = "componentOf"
    # CONNECTED_TO                 = "connectedTo"
    #
    TEMPLATE_ID                   = "templateId"
    # TEMPLATE                     = "template"
    # CONFIGID                     = "configId"
    # SUBJECT                        = "subject"
    # ALERT_UUID                    = "uuId"
    # DESCRIPTION                = "description"
    # IS_RESOLVED                    = " is Resolved"
    MOID                         = "moId"
    SOURCE_MOID                  = "sourceId"
    TARGET_MOID                  = "targetId"
    # RESOURCEUUID                 = "resourceUUID"
    #
    # HTTPS                        = "https"
    # HTTP                            = "http"
    IPADDRESS                   =  "ipAddress"
    PROTOCOL                    = "isSecure"
    USERNAME                        = "username"
    PASSWORD                        = "password"
    #
    ID                            = "id"
    NAME                            = "name"
    TYPE                            = "type"
    SYSTEM_VERSION_NAME            = "systemVersionName"
    SW_ID                           = "swid"
    PROTECTION_DOMAIN_ID            = "protectionDomainId"
    SYSTEM_ID                    = "systemId"
    SDC_IP                        = "sdcIp"
    VERSION_INFO                    = "versionInfo"
    OS_TYPE                        = "osType"
    OS                             = "os"
    TAGS                           = "tags"
    SOFT_VERSION_INFO            = "softwareVersionInfo"
    STORAGEPOOL_ID                = "storagePoolId"
    # FIRMWARE_VERSION                = "firmwareVersion"
    SERIAL_NUMBER                  = "serialNumber"
    MODEL_NAME                    = "modelName"
    MODEL                          = "model"
    RESOURCE_NAME                  ="resourceName"
    HOST_NAME                      = "hostName"
    MDM_CLUSTER                    = "mdmCluster"
    MASTER                         = "master"
    MANAGEMENT_IP                = "managementIPs"
    PORT                            = "port"
    # TYPE                            = "Type"
    SDC_TYPE                        = "sdcType"
    SIZE                        = "sizeInKb"
    SIZE_IN_KB                        = "Size In Kb"
    VOLUMETYPE                     = "volumeType"
    VOLUME_TYPE                    = "Volume Type"
    # VERSION                        = "Version"
    DEVICETYPE                    = "deviceType"
    DEVICE_TYPE                    = "Device Type"

    MEDIA_TYPE                    = "Media Type"
    MEDIATYPE                      = "mediaType"

    VENDORNAME                    = "vendorName"
    VENDOR_NAME                    = "Vendor Name"
    HYPHEN                        = "-"
    # ALERTNOTIFICATIONSTORE        = "alertNotificationStore"
    # CRITICAL                    = "Critical"
    # WARNING                        = "Warning"
    # INFO                        = "Info"
    # OK                        = "Ok"
    # POWERFLEX_EVENTS                = "Dell PowerFlex Events"
    #
    # # native types
    SYSTEM                        = "System"
    MDM                           = "Mdm"
    SDC                            = "Sdc"
    PROTECTION_DOMAIN            = "ProtectionDomain"
    STORAGE_POOL                    = "StoragePool"
    SDS                            = "Sds"
    VOLUME                        = "Volume"
    # VTREE                        = "VTree"
    DEVICE                        = "Device"
    # SPSDS                        = "SpSds"
    #
    STATISTICS                       ="Statistics"
    METRIC_NAME                     ="metricName"
    INSTANCE_VALUE                  ="instanceVal"
    TIME_STAMP                      ="ts"

    START_PATTERN                     ="$."
    MDM_PATTERN                        = "$.mdmCluster."



    # JSON                            = ".json"
    # STATISTICS_JSON                = "_Statistics.json"
    # INSTANCE_JSON                = "_Instance.json"
    #
    SYSTEM_NATIVE_TYPE            = "Dell PowerFlex System"
    MDM_NATIVE_TYPE                = "Dell PowerFlex MDM Cluster"
    SDC_NATIVE_TYPE                = "Dell PowerFlex SDC"
    PROTECTION_DOMAIN_NATIVE_TYPE= "Dell PowerFlex Protection Domain"
    STORAGE_POOL_NATIVE_TYPE        = "Dell PowerFlex Storage Pool"
    SDS_NATIVE_TYPE                = "Dell PowerFlex SDS"
    VOLUME_NATIVE_TYPE            = "Dell PowerFlex Volume"
    # VTREE_NATIVE_TYPE            = "Dell PowerFlex VTree"
    DEVICE_NATIVE_TYPE            = "Dell PowerFlex Device"
    # SPSDS_NATIVE_TYPE            = "Dell PowerFlex SpSds"
    #
    UNUSED_CAPACITY                = "unusedCapacityInKb"
    # REBALANCE_CAPACITY            = "rebalanceCapacityInKb"
    # SNAP_CAPACITY                = "snapCapacityInUseInKb"
    # USER_DATA_CAPACITY            = "maxUserDataCapacityInKb"
    # THICK_CAPACITY                = "thickCapacityInUseInKb"
    # THIN_CAPACITY                = "thinCapacityInUseInKb"
    MAX_CAPACITY                    = "maxCapacityInKb"
    # CLUSTER_STATE                = "clusterState"
    CLUSTER_NORMAL                = "ClusteredNormal"
    # DEVICE_STATE                    = "deviceState"
    NORMAL                        = "Normal"
    CONNECTED                    = "Connected"
    # SDS_STATE                    = "sdsState"
    MDM_CONNECTION_STATE            = "mdmConnectionState"
    # PROTECTION_DOMAIN_STATE        = "protectionDomainState"
    ACTIVE                        = "Active"
    # CAPACITY_USAGE_STATE            = "capacityUsageState"
    #
    # // Metric names
    # STORAGEPOOL_ACTIVE_BCK_REBUILD_CAPACITY       = "dell_powerflex_storagePool_ActiveBckRebuildCapacity"
    # STORAGEPOOL_ACTIVE_FWD_REBUILD_CAPACITY       = "dell_powerflex_storagePool_ActiveFwdRebuildCapacity"
    # STORAGEPOOL_ACTIVE_MOVING_CAPACITY            = "dell_powerflex_storagePool_ActiveMovingCapacity"
    # STORAGEPOOL_ACTIVE_NORM_REBUILD_CAPACITY      = "dell_powerflex_storagePool_ActiveNormRebuildCapacity"
    # STORAGEPOOL_ACTIVE_REBALANCE_CAPACITY         = "dell_powerflex_storagePool_ActiveRebalanceCapacity"
    # STORAGEPOOL_AT_REST_CAPACITY                 = "dell_powerflex_storagePool_AtRestCapacity"
    # STORAGEPOOL_BCK_REBUILD_CAPACITY              = "dell_powerflex_storagePool_BckRebuildCapacity"
    # STORAGEPOOL_CAPCITY_AVAILABLE_VOLUME          = "dell_powerflex_storagePool_CapacityAvailableForVolumeAllocation"
    # STORAGEPOOL_CAPACITY_IN_USE                   = "dell_powerflex_storagePool_CapacityInUse"
    # STORAGEPOOL_CAPACITY_LIMIT                    = "dell_powerflex_storagePool_CapacityLimit"
    # STORAGEPOOL_DEGRADED_FAILED_CAPACITY          = "dell_powerflex_storagePool_DegradedFailedCapacity"
    # STORAGEPOOL_DEGRADED_HEALTHY_CAPACITY         = "dell_powerflex_storagePool_DegradedHealthyCapacity"
    # STORAGEPOOL_FAILED_CAPACITY                   = "dell_powerflex_storagePool_FailedCapacity"
    # STORAGEPOOL_FWD_REBUILD_CAPACITY              = "dell_powerflex_storagePool_FwdRebuildCapacity"
    # STORAGEPOOL_MAINTENANCE_CAPACITY              = "dell_powerflex_storagePool_InMaintenanceCapacity"
    # STORAGEPOOL_MAX_CAPACITY                      = "dell_powerflex_storagePool_MaxCapacity"
    # STORAGEPOOL_MOVING_CAPACITY                   = "dell_powerflex_storagePool_MovingCapacity"
    # STORAGEPOOL_NORM_REBUILD_CAPACITY             = "dell_powerflex_storagePool_NormRebuildCapacity"
    # STORAGEPOOL_NUM_OF_DEVICES                    = "dell_powerflex_storagePool_NumOfDevices"
    # STORAGEPOOL_NUM_OF_VOLUMES                    = "dell_powerflex_storagePool_NumOfVolumes"
    # STORAGEPOOL_NUM_OF_VTREE                     = "dell_powerflex_storagePool_NumOfVtrees"
    # STORAGEPOOL_PENDING_BCK_REBUILD_CAPACITY      = "dell_powerflex_storagePool_PendingBckRebuildCapacity"
    # STORAGEPOOL_PENDING_FWD_REBUILD_CAPACITY      = "dell_powerflex_storagePool_PendingFwdRebuildCapacity"
    # STORAGEPOOL_PENDING_MOVING_CAPACITY           = "dell_powerflex_storagePool_PendingMovingCapacity"
    # STORAGEPOOL_PENDING_NORM_REBUILD_CAPACITY     = "dell_powerflex_storagePool_PendingNormRebuildCapacity"
    # STORAGEPOOL_PENDING_REBALANCE_CAPACITY        = "dell_powerflex_storagePool_PendingRebalanceCapacity"
    # STORAGEPOOL_PROTECTED_CAPACITY                = "dell_powerflex_storagePool_ProtectedCapacity"
    # STORAGEPOOL_REBALANCE_CAPACITY                = "dell_powerflex_storagePool_RebalanceCapacity"
    # STORAGEPOOL_SEMI_PROTECTED_CAPACITY           = "dell_powerflex_storagePool_SemiProtectedCapacity"
    # STORAGEPOOL_SNAP_CAPACITY_INUSE               = "dell_powerflex_storagePool_SnapCapacityInUse"
    # STORAGEPOOL_SNAP_CAPACITY_OCCUPIED            = "dell_powerflex_storagePool_SnapCapacityInUseOccupied"
    # STORAGEPOOL_SPARE_CAPACITY                     = "dell_powerflex_storagePool_SpareCapacity"
    # STORAGEPOOL_THICK_CAPACITY_INUSE              = "dell_powerflex_storagePool_ThickCapacityInUse"
    # STORAGEPOOL_THIN_CAPACITY_ALLOCATED           = "dell_powerflex_storagePool_ThinCapacityAllocated"
    # STORAGEPOOL_THIN_CAPACITY_ALLOCATED_IN_KM     = "dell_powerflex_storagePool_ThinCapacityAllocatedInKm"
    # STORAGEPOOL_THIN_CAPACITY_INUSE               = "dell_powerflex_storagePool_ThinCapacityInUse"
    # STORAGEPOOL_UNREACHABLE_UNUSED_CAPACITY       = "dell_powerflex_storagePool_UnreachableUnusedCapacity"
    # STORAGEPOOL_UNUSED_CAPACITY                     = "dell_powerflex_storagePool_UnusedCapacity"
    # STORAGEPOOL_RFACHE_READ_HIT                   = "dell_powerflex_storagePool_RfacheReadHit"
    # STORAGEPOOL_RFACHE_WRITE_HIT                  = "dell_powerflex_storagePool_RfacheWriteHit"
    # STORAGEPOOL_RFCACHE_AVG_READ_TIME             = "dell_powerflex_storagePool_RfcacheAvgReadTime"
    # STORAGEPOOL_RFCACHE_AVG_WRITE_TIME            = "dell_powerflex_storagePool_RfcacheAvgWriteTime"
    # STORAGEPOOL_RFCACHE_READ_MISS                 = "dell_powerflex_storagePool_RfcacheReadMiss"
    # STORAGEPOOL_RFCACHE_READS_FROM_CACHE          = "dell_powerflex_storagePool_RfcacheReadsFromCache"
    # STORAGEPOOL_RFCACHE_READ_PENDING              = "dell_powerflex_storagePool_RfcacheReadsPending"
    # STORAGEPOOL_RFCACHE_READ_RECEIVED             = "dell_powerflex_storagePool_RfcacheReadsReceived"
    # STORAGEPOOL_RFCACHE_READ_SKIPPED              = "dell_powerflex_storagePool_RfcacheReadsSkipped"
    # STORAGEPOOL_RFCACHE_READ_SKIPPED_ALIGNED_SIZE = "dell_powerflex_storagePool_RfcacheReadsSkippedAlignedSizeTooLarge"
    # STORAGEPOOL_RFCACHE_READ_SKIPPED_HEAVY_LOAD   = "dell_powerflex_storagePool_RfcacheReadsSkippedHeavyLoad"
    # STORAGEPOOL_RFCACHE_READ_SKIPPED_INTERNAL_ERROR= "dell_powerflex_storagePool_RfcacheReadsSkippedInternalError"
    # STORAGEPOOL_RFCACHE_READ_SKIPPED_LOCK_IOS     = "dell_powerflex_storagePool_RfcacheReadsSkippedLockIos"
    # STORAGEPOOL_RFCACHE_READ_SKIPPED_LOW_RESOURCES= "dell_powerflex_storagePool_RfcacheReadsSkippedLowResources"
    # STORAGEPOOL_RFCACHE_READ_SKIPPED_MAX_IO_SIZE  = "dell_powerflex_storagePool_RfcacheReadsSkippedMaxIoSize"
    # STORAGEPOOL_RFCACHE_READ_SKIPPED_STUCK_IO     = "dell_powerflex_storagePool_RfcacheReadsSkippedStuckIo"
    # STORAGEPOOL_RFCACHE_SKIPPED_UNLINED_WRITE     = "dell_powerflex_storagePool_RfcacheSkippedUnlinedWrite"
    # STORAGEPOOL_RFCACHE_SOURCE_DEVICE_READS       = "dell_powerflex_storagePool_RfcacheSourceDeviceReads"
    # STORAGEPOOL_RFCACHE_SOURCE_DEVICE_WRITE       = "dell_powerflex_storagePool_RfcacheSourceDeviceWrites"
    # STORAGEPOOL_RFCACHE_WRITE_MISS                = "dell_powerflex_storagePool_RfcacheWriteMiss"
    # STORAGEPOOL_RFCACHE_WRITE_PENDING             = "dell_powerflex_storagePool_RfcacheWritePending"
    # STORAGEPOOL_RFCACHE_WRITE_RECEIVED            = "dell_powerflex_storagePool_RfcacheWritesReceived"
    # STORAGEPOOL_RFCACHE_WRITE_SKIPPED_CACHE_MISS  = "dell_powerflex_storagePool_RfcacheWritesSkippedCacheMiss"
    # STORAGEPOOL_RFCACHE_WRITE_SKIPPED_HEAVY_LOAD  = "dell_powerflex_storagePool_RfcacheWritesSkippedHeavyLoad"
    # STORAGEPOOL_RFCACHE_WRITE_SKIPPED_INTERNAL    = "dell_powerflex_storagePool_RfcacheWritesSkippedInternalError"
    # STORAGEPOOL_RFCACHE_WRITE_SKIPPED_RESOURCES   = "dell_powerflex_storagePool_RfcacheWritesSkippedLowResources"
    # STORAGEPOOL_RFCACHE_WRITE_SKIPPED_MAX_IO_SIZE = "dell_powerflex_storagePool_RfcacheWritesSkippedMaxIoSize"
    # STORAGEPOOL_RFCACHE_WRITE_SKIPPED_STUCK_IO    = "dell_powerflex_storagePool_RfcacheWritesSkippedStuckIo"
    STOREAGE_POOL_STATE                             = "dell_powerflex_storagePool_UsageState"
    #
    # SYSTEM_AVAILABLE_CAPACITY                     = "dell_powerflex_system_AvailableCapacity"
    # SYSTEM_REBALANCE_CAPACITY                     = "dell_powerflex_system_RebalanceCapacity"
    # SYSTEM_SNAP_USED_CAPACITY                     = "dell_powerflex_system_SnapUsedCapacity"
    # SYSTEM_CAPACITY                             = "dell_powerflex_system_SystemCapacity"
    # SYSTEM_THICK_USED_CAPACITY                     = "dell_powerflex_system_ThickUsedCapacity"
    # SYSTEM_THIN_USED_CAPACITY                     = "dell_powerflex_system_ThinUsedCapacity"
    SYSTEM_TOTAL_USED_CAPACITY                     = "dell_powerflex_system_TotalUsedCapacity"
    # SYSTEM_UNUSABLE_CAPACITY                         = "dell_powerflex_system_UnusableCapacity"
    SYSTEM_CAPACITY_UTILIZATION                   = "dell_powerflex_system_CapacityUtilization"
    #
    MDM_CLUSTER_STATE_METRIC                         = "dell_powerflex_mdm_CurrentState"
    SDS_STATE_METRIC                                 = "dell_powerflex_sds_ConnectionState"
    SDC_STATE_METRIC                                 = "dell_powerflex_sdc_ConnectionState"
    PROTECTION_DOMAIN_STATE_METRIC                 = "dell_powerflex_protectionDomain_State"
    DEVICE_STATE_METRIC                         = "dell_powerflex_device_State"
    # SYSTEM_ALERT_METRIC                         = "dell_powerflex_event_Statistics"
    # TOTAL_EVENT_COUNT                         = "totalEventsCount"
    # CURRENT_EVENT_COUNT                         = "currentEventsCount"



    # ACTIVE_BCK_REBUILD_CAPACITY       = "activeBckRebuildCapacityInKb"
    # ACTIVE_FWD_REBUILD_CAPACITY       = "activeFwdRebuildCapacityInKb"
    # ACTIVE_MOVING_CAPACITY            = "activeMovingCapacityInKb"
    # ACTIVE_NORM_REBUILD_CAPACITY      = "activeNormRebuildCapacityInKb"
    # ACTIVE_REBALANCE_CAPACITY         = "activeRebalanceCapacityInKb"
    # AT_REST_CAPACITY                 = "atRestCapacityInKb"
    # BCK_REBUILD_CAPACITY              = "bckRebuildCapacityInKb"
    # CAPCITY_AVAILABLE_VOLUME          = "capacityAvailableForVolumeAllocationInKb"
    # CAPACITY_IN_USE                   = "capacityInUseInKb"
    # CAPACITY_LIMIT                    = "capacityLimitInKb"
    # DEGRADED_FAILED_CAPACITY          = "degradedFailedCapacityInKb"
    # DEGRADED_HEALTHY_CAPACITY         = "degradedHealthyCapacityInKb"
    # FAILED_CAPACITY                   = "failedCapacityInKb"
    # FWD_REBUILD_CAPACITY              = "fwdRebuildCapacityInKb"
    # MAINTENANCE_CAPACITY              = "inMaintenanceCapacityInKb"
    # MOVING_CAPACITY                   = "movingCapacityInKb"
    # NORM_REBUILD_CAPACITY             = "normRebuildCapacityInKb"
    # NUM_OF_DEVICES                    = "numOfDevices"
    # NUM_OF_VOLUMES                    = "numOfVolumes"
    # NUM_OF_VTREE                     = "numOfVtrees"
    # PENDING_BCK_REBUILD_CAPACITY      = "pendingBckRebuildCapacityInKb"
    # PENDING_FWD_REBUILD_CAPACITY      = "pendingFwdRebuildCapacityInKb"
    # PENDING_MOVING_CAPACITY           = "pendingMovingCapacityInKb"
    # PENDING_NORM_REBUILD_CAPACITY     = "pendingNormRebuildCapacityInKb"
    # PENDING_REBALANCE_CAPACITY        = "pendingRebalanceCapacityInKb"
    # PROTECTED_CAPACITY                = "protectedCapacityInKb"
    # SEMI_PROTECTED_CAPACITY           = "semiProtectedCapacityInKb"
    # SNAP_CAPACITY_INUSE               = "snapCapacityInUseInKb"
    # SNAP_CAPACITY_OCCUPIED            = "snapCapacityInUseOccupiedInKb"
    # SPARE_CAPACITY                     = "spareCapacityInKb"
    # THICK_CAPACITY_INUSE              = "thickCapacityInUseInKb"
    # THIN_CAPACITY_ALLOCATED           = "thinCapacityAllocatedInKb"
    # THIN_CAPACITY_ALLOCATED_IN_KM     = "thinCapacityAllocatedInKm"
    # THIN_CAPACITY_INUSE               = "thinCapacityInUseInKb"
    # UNREACHABLE_UNUSED_CAPACITY       = "unreachableUnusedCapacityInKb"
    # RFACHE_READ_HIT                   = "rfacheReadHit"
    # RFACHE_WRITE_HIT                  = "rfacheWriteHit"
    # RFCACHE_AVG_READ_TIME             = "rfcacheAvgReadTime"
    # RFCACHE_AVG_WRITE_TIME            = "rfcacheAvgWriteTime"
    # RFCACHE_READ_MISS                 = "rfcacheReadMiss"
    # RFCACHE_READS_FROM_CACHE          = "rfcacheReadsFromCache"
    # RFCACHE_READ_PENDING              = "rfcacheReadsPending"
    # RFCACHE_READ_RECEIVED             = "rfcacheReadsReceived"
    # RFCACHE_READ_SKIPPED              = "rfcacheReadsSkipped"
    # RFCACHE_READ_SKIPPED_ALIGNED_SIZE = "rfcacheReadsSkippedAlignedSizeTooLarge"
    # RFCACHE_READ_SKIPPED_HEAVY_LOAD   = "rfcacheReadsSkippedHeavyLoad"
    # RFCACHE_READ_SKIPPED_INTERNAL_ERROR= "rfcacheReadsSkippedInternalError"
    # RFCACHE_READ_SKIPPED_LOCK_IOS     = "rfcacheReadsSkippedLockIos"
    # RFCACHE_READ_SKIPPED_LOW_RESOURCES= "rfcacheReadsSkippedLowResources"
    # RFCACHE_READ_SKIPPED_MAX_IO_SIZE  = "rfcacheReadsSkippedMaxIoSize"
    # RFCACHE_READ_SKIPPED_STUCK_IO     = "rfcacheReadsSkippedStuckIo"
    # RFCACHE_SKIPPED_UNLINED_WRITE     = "rfcacheSkippedUnlinedWrite"
    # RFCACHE_SOURCE_DEVICE_READS       = "rfcacheSourceDeviceReads"
    # RFCACHE_SOURCE_DEVICE_WRITE       = "rfcacheSourceDeviceWrites"
    # RFCACHE_WRITE_MISS                = "rfcacheWriteMiss"
    # RFCACHE_WRITE_PENDING             = "rfcacheWritePending"
    # RFCACHE_WRITE_RECEIVED            = "rfcacheWritesReceived"
    # RFCACHE_WRITE_SKIPPED_CACHE_MISS  = "rfcacheWritesSkippedCacheMiss"
    # RFCACHE_WRITE_SKIPPED_HEAVY_LOAD  = "rfcacheWritesSkippedHeavyLoad"
    # RFCACHE_WRITE_SKIPPED_INTERNAL    = "rfcacheWritesSkippedInternalError"
    # RFCACHE_WRITE_SKIPPED_RESOURCES   = "rfcacheWritesSkippedLowResources"
    # RFCACHE_WRITE_SKIPPED_MAX_IO_SIZE = "rfcacheWritesSkippedMaxIoSize"
    # RFCACHE_WRITE_SKIPPED_STUCK_IO    = "rfcacheReadsSkippedStuckIo"
