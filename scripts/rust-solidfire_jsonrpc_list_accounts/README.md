## Example of using the SolidFire API from Rust

- Method `ListAccounts`

## How 

- Edit `Config.toml` (SolidFire MVIP, cluster account, password)
- In the same directory, run `cargo build`
- Run the built debug example with `./target/debug/solidfire_jsonrpc_list_accounts`

```sh
$ ./target/debug/solidfire_jsonrpc_list_accounts 
Account: sean (ID: 1)
  Status: active
  Volumes: Some([10, 11, 13, 15, 97])

Account: rocky94 (ID: 2)
  Status: active
  Volumes: Some([20, 21, 22, 23, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85])

Account: k3sdr (ID: 3)
  Status: active
  Volumes: Some([])

```


## Environment and version information

- SolidFire 12.5 with snake-oil TLS certificate (you may enable validation in L72)
- `cargo 1.85.1 (d73d2caf9 2024-12-31)`
- Ubuntu 24.04 LTS OS
