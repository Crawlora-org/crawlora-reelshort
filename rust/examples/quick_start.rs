use crawlora_reelshort::{Client, ModelReelshortHomeResponseDoc, ReelshortHomeParams};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .reelshort
        .home(ReelshortHomeParams {
            ..Default::default()
        })
        .await?;
    let data: ModelReelshortHomeResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
