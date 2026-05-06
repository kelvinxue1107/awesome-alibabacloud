import re

with open('README.md', 'r') as f:
    content = f.read()

replacements = {
    # Compute
    "Azure-VM-blue": "Azure-Virtual_Machines-blue",
    "Google_Cloud_Functions-skyblue": "Cloud_Functions-skyblue",
    "Azure-Azure_Dedigated_Host-blue": "Azure-Dedicated_Host-blue",
    "AWS-EC2_Dedigated_Hosts-orange": "AWS-EC2_Dedicated_Hosts-orange",
    
    # Storage
    "GCP-Cloud_Storage_Buckets-skyblue": "GCP-Cloud_Storage-skyblue",
    "Azure-Disk_Storage-blue": "Azure-Managed_Disks-blue",
    "Azure-StorSimple-blue": "Azure-Azure_Stack_Edge-blue",
    "Azure-DataBox-blue": "Azure-Data_Box-blue",
    "GCP-TransferAppliance-skyblue": "GCP-Transfer_Appliance-skyblue",
    "GCP-BackupAndDisasterRecovery-skyblue": "GCP-Backup_and_DR-skyblue",
    
    # Database
    "AWS-Aurora-orange": "AWS-RDS_for_SQL_Server-orange",
    "GCP-CloudSpanner-skyblue": "GCP-Cloud_SQL_for_SQL_Server-skyblue",
    "Azure-SQLDatabase-blue": "Azure-SQL_Database-blue",
    "Azure-CosmodDB-blue": "Azure-Cosmos_DB-blue",
    "Azure-CosmosDB-blue": "Azure-Cosmos_DB-blue",
    "GCP-CloudBitTable-skyblue": "GCP-Cloud_Bigtable-skyblue",
    "GCP-CloudBigTable-skyblue": "GCP-Cloud_Bigtable-skyblue",
    "Azure-N/A-blue": "Azure-Cosmos_DB-blue",
    "Azure-Cache4Redis-blue": "Azure-Cache_for_Redis-blue",
    "Azure-TimeSeriesInsights-blue": "Azure-Data_Explorer-blue",
    "Azure-Blockchain_Service-blue": "Azure-Confidential_Ledger-blue",

    # NoSQL Key-Value specific fix (ApsaraDB for MongoDB to Table Store)
    "**********[ApsaraDB for MongoDB](https://www.alibabacloud.com/product/apsaradb-for-mongodb)| ![Static Badge](https://img.shields.io/badge/Azure-Cosmos_DB-blue)  | ![Static Badge](https://img.shields.io/badge/AWS-DynamoDB-orange) | ![Static Badge](https://img.shields.io/badge/GCP-Cloud_Bigtable-skyblue)**********": "**********[Table Store](https://www.alibabacloud.com/product/table-store)| ![Static Badge](https://img.shields.io/badge/Azure-Cosmos_DB-blue)  | ![Static Badge](https://img.shields.io/badge/AWS-DynamoDB-orange) | ![Static Badge](https://img.shields.io/badge/GCP-Cloud_Bigtable-skyblue)**********",

    # Analytics
    "AWS-RedShift-orange": "AWS-Redshift-orange",
    "Azure-Data_Explorer-blue": "Azure-HDInsight-blue",
    "Azure-Power_BI_Embedded-blue": "Azure-Power_BI-blue",
    "AWS-Quicksight-orange": "AWS-QuickSight-orange",
    "Azure-Stream_Analytics,_Event_Hubs-blue": "Azure-Stream_Analytics-blue",
    "AWS-EC2-orange": "AWS-Kinesis_Data_Analytics-orange",
    "GCP-ComputeEngine-skyblue": "GCP-Dataflow-skyblue",
    "Azure-Data_Factory-blue": "Azure-Data_Factory-blue", # No change, but safe
    "AWS-Glue,_Kinesis_Data_Firehose,_SageMaker,_Data_Wrangler-orange": "AWS-Glue-orange",
    "AWS-Data_pipeline-orange": "AWS-Step_Functions-orange",
    "GCP-Cloud_Storage-skyblue": "GCP-Cloud_Composer-skyblue",
    "Azure-Data_Share-blue": "Azure-Data_Lake_Storage-blue",
    "GCP-Cloud_Search-skyblue": "GCP-Dataproc-skyblue",
    "Azure-Cognitive_Search-blue": "Azure-AI_Search-blue",
    "AWS-CloudSearch,_OpenSearch_Service,_Kendra-orange": "AWS-OpenSearch_Service-orange",
    
    # ML and AI
    "Azure-Machine_Learning_Studio,_Automated_ML-blue": "Azure-Machine_Learning-blue",
    "GCP-Vertex_AI_Workbench-skyblue": "GCP-Vertex_AI-skyblue",
    "Azure-Text_Analytics-blue": "Azure-Language_Service-blue",
    "Azure-Cognitive_Services_for_Vision-blue": "Azure-AI_Vision-blue",
    "AWS-Rekognition,_Panorama,_Lookout_for_Vision-orange": "AWS-Rekognition-orange",
    "Azure-Cognitive_Services_for_Speech_to_Text-blue": "Azure-Speech_Service-blue",
    "GCP-SpeechToText-skyblue": "GCP-Speech_to_Text-skyblue",
    "Azure-Cognitive_Services_for_Text_to_Speech-blue": "Azure-Speech_Service-blue",
    "GCP-TextToSpeech-skyblue": "GCP-Text_to_Speech-skyblue",
    "Azure-Cognitive_Services_for_Speech_Translation,_Translator-blue": "Azure-Translator-blue",

    # Networking
    "Azure-Content_Delivery_Network-blue": "Azure-CDN-blue",
    "GCP-Cloud_CDN_and_Media_CDN-skyblue": "GCP-Cloud_CDN-skyblue",
    "Azure-API_Apps,_API_Management-blue": "Azure-API_Management-blue",
    "GCP-Apigee_API_Management-skyblue": "GCP-API_Gateway-skyblue",
    "Azure-Application_Gateway,_Load_Balancer,_Traffic_Manager-blue": "Azure-Load_Balancer-blue",

    # Containers
    "Azure-ACR-blue": "Azure-Container_Instances-blue", # Note: Watch out for ECI vs ACR. I will handle this specifically later if needed.
    "AWS-ECR-orange": "AWS-Fargate-orange",
    "GCP-ContainerRegistry-skyblue": "GCP-Cloud_Run-skyblue",
    
    # Management
    "Azure-IAM-blue": "Azure-Entra_ID-blue",
    "AWS-Entra_ID-orange": "AWS-IAM-orange",
    "GCP-Cloud_Identity-skyblue": "GCP-IAM-skyblue",
    "Azure-Monitor_Activity_Log-blue": "Azure-Azure_Monitor-blue",
    "GCP-Access_Transparency_and_Access_approval-skyblue": "GCP-Cloud_Audit_Logs-skyblue",
    "Azure-Security-blue": "Azure-Defender_for_Cloud-blue",
    "Azure-Monitor,_Anomaly_Detctor-blue": "Azure-Azure_Monitor-blue",
    "GCP-Operations,_Network_Intelligence_Center-skyblue": "GCP-Cloud_Monitoring-skyblue",
    "Azure-Automation-blue": "Azure-Azure_Automation-blue",
    "AWS-OpsWorks-orange": "AWS-Systems_Manager-orange",
    "GCP-Compute_Engine_Management-skyblue": "GCP-Deployment_Manager-skyblue"
}

for k, v in replacements.items():
    content = content.replace(k, v)

# Specific fixes for lines where replace might have matched incorrectly or we need more precise match
# For Container registry (ACR), we might have accidentally replaced it with Container_Instances because of the ACR rule above
content = content.replace(
    "[Container Registry (ACR)](https://www.alibabacloud.com/product/container-registry).       | ![Static Badge](https://img.shields.io/badge/Azure-Container_Instances-blue) | ![Static Badge](https://img.shields.io/badge/AWS-Fargate-orange) | ![Static Badge](https://img.shields.io/badge/GCP-Cloud_Run-skyblue)",
    "[Container Registry (ACR)](https://www.alibabacloud.com/product/container-registry).       | ![Static Badge](https://img.shields.io/badge/Azure-ACR-blue) | ![Static Badge](https://img.shields.io/badge/AWS-ECR-orange) | ![Static Badge](https://img.shields.io/badge/GCP-Artifact_Registry-skyblue)"
)

# Fix Vertex AI search which was Cloud_Search before
content = content.replace(
    "![Static Badge](https://img.shields.io/badge/GCP-Dataproc-skyblue)**********\n\n### **********Managed search**********\n\n* **********[Alibaba Cloud Elasticsearch](https://www.alibabacloud.com/product/elasticsearch) | ![Static Badge](https://img.shields.io/badge/Azure-AI_Search-blue)  | ![Static Badge](https://img.shields.io/badge/AWS-OpenSearch_Service-orange) | ![Static Badge](https://img.shields.io/badge/GCP-Dataproc-skyblue)",
    "![Static Badge](https://img.shields.io/badge/GCP-Dataproc-skyblue)**********\n\n### **********Managed search**********\n\n* **********[Alibaba Cloud Elasticsearch](https://www.alibabacloud.com/product/elasticsearch) | ![Static Badge](https://img.shields.io/badge/Azure-AI_Search-blue)  | ![Static Badge](https://img.shields.io/badge/AWS-OpenSearch_Service-orange) | ![Static Badge](https://img.shields.io/badge/GCP-Vertex_AI_Search-skyblue)"
)

with open('README.md', 'w') as f:
    f.write(content)

print("Replacement complete.")
