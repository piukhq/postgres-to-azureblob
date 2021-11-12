# postgres-to-azureblob

Simple Python application for backing up a single PostgreSQL Database and storing the output on Azure Blob Storage.

# Deployment and Usage

Deployment via a `kustomization.yaml` file can make this easy to tweak for your specific needs and makes this simple to deploy via Flux 2 or similar.

```yaml
bases:
  - github.com/binkhq/postgres-to-azureblob/deploy

patches:
  - target:
      kind: CronJob
    patch: |-
      - op: replace
        path: /metadata/name
        value: hourly-backup
  - target:
      kind: CronJob
    patch: |-
      - op: replace
        path: /spec/schedule
        value: "30 * * * *"
  - target:
      kind: CronJob
    patch: |-
      - op: replace
        path: /spec/jobTemplate/spec/template/spec/containers/0/env
        value:
          - name: blob_storage_connection_string
            valueFrom:
              secretKeyRef:
                key: connection_string
                name: azure-storage-common
          - name: blob_storage_container
            value: backups
          - name: blob_storage_path_prefix
            value: hourly
          - name: psql_connection_string
            valueFrom:
              secretKeyRef:
                key: common_postgres
                name: azure-pgfs
```

# Notes

This project does not support Azure Database for PostgreSQL Single Server due to its non-standard connection strings, we only test on Azure Database for PostgreSQL Flexible Server and standard PostgreSQL installations.
