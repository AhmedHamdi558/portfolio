/**
 * BUILDER: AHMED HAMDI
 * ROLE: AUTOMATION & SOFTWARE DEVELOPER
 * VERSION: 2.1 (SIMPLIFIED DEMO)
 */

"use strict";

const {
    default: makeWASocket,
    useMultiFileAuthState,
    delay,
    DisconnectReason,
    fetchLatestBaileysVersion
} = require("@whiskeysockets/baileys");
const pino = require("pino");
const readline = require("readline");

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const question = (text) => new Promise((resolve) => rl.question(text, resolve));

async function startBot() {
    const { state, saveCreds } = await useMultiFileAuthState("session_auth");
    const { version } = await fetchLatestBaileysVersion();

    const sock = makeWASocket({
        version,
        auth: state,
        printQRInTerminal: false, // سنستخدم نظام كود الربط
        logger: pino({ level: "silent" }),
        browser: ["Ubuntu", "Chrome", "20.0.04"]
    });

    // طلب كود الربط إذا لم تكن هناك جلسة مسجلة
    if (!sock.authState.creds.registered) {
        const phoneNumber = await question("يرجى ادخال رقم الهاتف (مثال: 216XXXXXXXX): ");
        const code = await sock.requestPairingCode(phoneNumber);
        console.log(`كود الربط الخاص بك هو: ${code}`);
    }

    sock.ev.on("creds.update", saveCreds);

    sock.ev.on("connection.update", (update) => {
        const { connection, lastDisconnect } = update;
        if (connection === "close") {
            const shouldReconnect = lastDisconnect.error?.output?.statusCode !== DisconnectReason.loggedOut;
            if (shouldReconnect) startBot();
        } else if (connection === "open") {
            console.log("تم الاتصال بنجاح. البوت جاهز للعمل.");
        }
    });

    // معالجة الرسائل الواردة
    sock.ev.on("messages.upsert", async (m) => {
        const msg = m.messages[0];
        if (!msg.message || msg.key.fromMe) return;

        const remoteJid = msg.key.remoteJid;
        const messageText = msg.message.conversation || msg.message.extendedTextMessage?.text;

        if (messageText) {
            const welcomeMessage = 
                "اهلا وسهلا بك\n\n" +
                "انا احمد حمدي، مطور برمجيات وأتمتة اعمال.\n" +
                "اقدم حلول ذكية لتوفير الوقت وزيادة الانتاجية عبر البرمجيات المخصصة.\n\n" +
                "تنبيه: هذا البوت هو مجرد نموذج تجريبي (Demo) لعرض القدرات التقنية على منصة واتساب.\n" +
                "يتم تصميم وبناء البوتات والخدمات البرمجية بشكل مخصص بالكامل حسب متطلبات كل مشروع.";

            await sock.sendMessage(remoteJid, { text: welcomeMessage });
        }
    });
}

startBot().catch(err => console.log("خطأ في التشغيل: " + err));
