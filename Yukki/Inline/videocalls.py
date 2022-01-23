from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def choose_markup(videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎵 Müzik Çal",
                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🎥 Video Oynat",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🗑 Aramayı Kapat",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def livestream_markup(quality, videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎥  Start Live",
                callback_data=f"LiveStream {quality}|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🗑 Kapat",
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def stream_quality_markup(videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="📽 360P",
                callback_data=f"VideoStream 360|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="📽 720P",
                callback_data=f"VideoStream 720|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="📽 480P",
                callback_data=f"VideoStream 480|{videoid}|{duration}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⇠ Geri Git",
                callback_data=f"gback_list_chose_stream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🗑 Aramayı Kapat",
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons
