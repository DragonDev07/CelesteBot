use crate::{Context, Error};

/// Pong!
#[poise::command(slash_command)]
pub async fn ping(ctx: Context<'_>) -> Result<(), Error> {
    let response = format!(":ping_pong: Pong!");
    ctx.say(response).await?;

    return Ok(());
}
