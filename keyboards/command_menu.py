from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command="/start", description="🚀 Запустить бота"),
        BotCommand(command="/help", description="ℹ️ Помощь"),
        BotCommand(command="/settings", description="⚙️ Настройки"),
        BotCommand(command="/cancel", description="❌ Отменить текущее действие")
    ]
    await bot.set_my_commands(main_menu_commands, BotCommandScopeDefault())
