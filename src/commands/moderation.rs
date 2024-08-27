use crate::{Context, Error};
use poise::serenity_prelude::User;

/// Kicks a member from the server.
#[poise::command(slash_command)]
pub async fn kick(
    ctx: Context<'_>,
    #[description = "Member to kick"] member: User,
    #[description = "Reason for kicking"] reason: Option<String>,
) -> Result<(), Error> {
    let guild_id = match ctx.guild_id() {
        Some(guild_id) => guild_id,
        None => {
            ctx.say("This command can only be used in a server.")
                .await?;
            return Ok(());
        }
    };

    let reason = reason.unwrap_or_else(|| "No reason provided".to_string());

    guild_id
        .kick_with_reason(&ctx.serenity_context().http, member.id, &reason)
        .await?;

    ctx.say(format!("Kicked {} for: {}", member.name, reason))
        .await?;

    return Ok(());
}

/// Bans a member from the server.
#[poise::command(slash_command)]
pub async fn ban(
    ctx: Context<'_>,
    #[description = "Member to ban"] member: User,
    #[description = "Reason for banning"] reason: Option<String>,
    #[description = "0-7 integer number of days worth of messages to delete"] days_messages: Option<
        u8,
    >,
) -> Result<(), Error> {
    let guild_id = match ctx.guild_id() {
        Some(guild_id) => guild_id,
        None => {
            ctx.say("This command can only be used in a server.")
                .await?;
            return Ok(());
        }
    };

    let reason = reason.unwrap_or_else(|| "No reason provided".to_string());
    let days_messages = days_messages.unwrap_or_else(|| 0);

    guild_id
        .ban_with_reason(
            &ctx.serenity_context().http,
            member.id,
            days_messages,
            &reason,
        )
        .await?;

    ctx.say(format!("Banned {} for: {}", member.name, reason))
        .await?;

    return Ok(());
}
