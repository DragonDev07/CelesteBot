use crate::{Context, Error};
use poise::builtins::register_globally;
use tracing::info;

const ALLOWED_USER_IDS: &[u64] = &[635175805261054004]; // Replace with actual user IDs
const ALLOWED_GUILD_ID: u64 = 1041478593257160744; // Replace with the actual guild ID

/// Reloads all commands.
#[poise::command(slash_command)]
pub async fn reload(ctx: Context<'_>) -> Result<(), Error> {
    // Check if the command is used in the allowed guild
    match ctx.guild_id() {
        Some(guild_id) if guild_id == ALLOWED_GUILD_ID => guild_id,
        _ => {
            info!(
                "User {} tried to run the `/reload` command in {}",
                ctx.author().name,
                ctx.guild_id().unwrap().get()
            );

            ctx.say("This command can only be used in the specific server.")
                .await?;

            return Ok(());
        }
    };

    // Check if the user is allowed to run the command
    let user_id = ctx.author().id.get();
    if !ALLOWED_USER_IDS.contains(&user_id) {
        ctx.say("You do not have permission to use this command.")
            .await?;
        return Ok(());
    }

    // Reload commands
    let framework = ctx.framework().clone();
    register_globally(ctx.serenity_context(), &framework.options().commands).await?;

    // Respond that commands have been reloaded
    ctx.say("Reloaded commands!").await?;

    return Ok(());
}
