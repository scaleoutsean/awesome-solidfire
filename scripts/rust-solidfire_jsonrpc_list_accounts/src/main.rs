use config::Config;
use reqwest::blocking::Client;
use reqwest::header::{HeaderMap, HeaderValue, CONTENT_TYPE};
use serde::{Deserialize, Serialize};
use std::error::Error;

#[derive(Deserialize)]
struct Settings {
    url: String,
    user: String,
    pass: String,
}

// Request structs
#[derive(Serialize)]
struct ListAccountsParams {
    #[serde(rename = "includeStorageContainers")]
    include_storage_containers: bool,
}

#[derive(Serialize)]
struct JsonRpcRequest<'a> {
    method: &'a str,
    params: ListAccountsParams,
    id: u32,
}

// Response structs
#[derive(Deserialize, Debug)]
struct Account {
    #[serde(rename = "accountID")]
    account_id: u32,
    username: String,
    status: String,
    volumes: Option<Vec<u32>>,
    // Add other fields as needed
}

#[derive(Deserialize, Debug)]
struct ListAccountsResult {
    accounts: Vec<Account>,
}

#[derive(Deserialize, Debug)]
struct JsonRpcResponse {
    id: u32,
    result: ListAccountsResult,
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let settings: Settings = Config::builder()
        .add_source(config::File::with_name("Config"))
        .build()?
        .try_deserialize()?;

    let url = &settings.url;
    let user = &settings.user;
    let pass = &settings.pass;

    let request = JsonRpcRequest {
        method: "ListAccounts",
        params: ListAccountsParams {
            include_storage_containers: false,
        },
        id: 1,
    };

    let mut headers = HeaderMap::new();
    headers.insert(CONTENT_TYPE, HeaderValue::from_static("application/json"));

    let client = Client::builder()
        .danger_accept_invalid_certs(true) // Remove for production!
        .default_headers(headers)
        .build()?;

    let resp = client
        .post(url)
        .basic_auth(user, Some(pass))
        .json(&request)
        .send()?;

    if !resp.status().is_success() {
        eprintln!("HTTP error: {}", resp.status());
        return Ok(());
    }

    let rpc_resp: JsonRpcResponse = resp.json()?;

    for acct in rpc_resp.result.accounts {
        println!(
            "Account: {} (ID: {})\n  Status: {}\n  Volumes: {:?}\n",
            acct.username, acct.account_id, acct.status, acct.volumes
        );
    }

    Ok(())
}