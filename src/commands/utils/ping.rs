use poise::CreateReply;

use crate::{Context, Error};

/// Pong!
#[poise::command(slash_command)]
pub async fn ping(ctx: Context<'_>) -> Result<(), Error> {
    let start_time = std::time::Instant::now();
    let msg = ctx.say("Pinging...").await?;

    let end_time = std::time::Instant::now();
    let ping = end_time.duration_since(start_time).as_millis();

    let reply = CreateReply::content(format!(":ping_pong: Pong! Latency: {}ms", ping));

    msg.edit(ctx, reply).await?;

    return Ok(());
}
