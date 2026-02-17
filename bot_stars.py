from aiogram import Bot, Dispatcher, types
from aiogram.types import LabeledPrice
from aiogram.filters import Command
import asyncio

BOT_TOKEN = "8511074927:AAFEUqSFXijnT6ZB3m-21Jo7kfKpkC17vB8"

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def inicio(message: types.Message):
    await message.answer("¡Bot listo! Usa /donar para enviar estrellas ⭐")

@dp.message(Command("donar"))
async def donar(message: types.Message):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Donación",
        description="Envía estrellas ⭐",
        payload="stars-payment",
        provider_token="",
        currency="XTR",
        prices=[LabeledPrice("Stars", 100)]
    )

@dp.pre_checkout_query()
async def aprobar_pago(query: types.PreCheckoutQuery):
    await query.answer(ok=True)

@dp.message(types.SuccessfulPayment)
async def pago_exitoso(message: types.Message):
    await message.answer("¡Estrellas recibidas! ✅⭐")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
