class config:
    BOT_TOKEN = "1759044800:AAE0yzWvTG9cWF25jCnIgamgY60h38uxIVI"
    APP_ID = "3026221"
    API_HASH = "0c210b8cce3360dd1a47eda938643845"
    DATABASE_URL = "postgres://pncnycrknktwaf:3f9a611aa85331c9d8742ccb136c2e9d1dfd29af31855ad5faca06ca2d140f8f@ec2-107-22-245-82.compute-1.amazonaws.com:5432/d866rvhal0e2i3"
    SUDO_USERS = "1218663244" # Sepearted by space.
    SUPPORT_CHAT_LINK = "https://t.me/Mizsuki"
    DOWNLOAD_DIRECTORY = "./downloads/"
    G_DRIVE_CLIENT_ID = "96046064335-k5n84rm4nnvl968kkb1c4fm49n05hsdd.apps.googleusercontent.com"
    G_DRIVE_CLIENT_SECRET = "sJLLmcHF-cAFwfBTd3Ltri4w"


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  YtDl = ['ytdl']

class Messages:
    START_MSG = "**Hi there {}.**\n__හායි 🖐මම පම්කයා 😍  මං බොම්ටෙක් 🤖 googledrive එකට ඕන රෙද්දක් අප්ලෝඩ් කරන්න මට ලින්ක් දාම්පන් 📤.__\n__You can know more from /help.__"

    HELP_MSG = [
        ".",
        "**Google Drive Uploader**\n__ googledrive එකට ඕන රෙද්දක් අප්ලෝඩ් කරන්න මට ලින්ක් දාම්පන් 📤 I can upload files from direct link or Telegram Files to your Google Drive. All i need is to authenticate me to your Google Drive Account and send a direct download link or Telegram File.__\n\nI have more features... ! Wanna know about it ? Just walkthrough this tutorial and read the messages carefully.",
        
        f"**Authenticating Google Drive**\n__Send the /{BotCommands.Authorize[0]} commmand and you will receive a URL, visit URL and follow the steps and send the received code here. Use /{BotCommands.Revoke[0]} to revoke your currently logged Google Drive Account.__\n\n**Note: I will not listen to any command or message (except /{BotCommands.Authorize[0]} command) until you authorize me.\nSo, Authorization is mandatory !**",
        
        f"**Direct Links**\n__Send me a direct download link for a file and i will download it on my server and Upload it to your Google Drive Account. You can rename files before uploading to GDrive Account. Just send me the URL and new filename separated by ' | '.__\n\n**__Examples:__**\n```https://example.com/AFileWithDirectDownloadLink.mkv | New FileName.mkv```\n\n**Telegram Files**\n__To Upload telegram files in your Google drive Account just send me the file and i will download and upload it to your Google Drive Account. Note: Telegram Files Downloading are slow. it may take longer for big files.__\n\n**YouTube-DL Support**\n__Download files via youtube-dl.\nUse /{BotCommands.YtDl[0]} (YouTube Link/YouTube-DL Supported site link)__",
        
        f"**Custom Folder for Upload**\n__Want to upload in custom folder or in__ **TeamDrive** __ ?\nUse /{BotCommands.SetFolder[0]} (Folder URL) to set custom upload folder.\nAll the files are uploaded in the custom folder you provide.__",
        
        f"**Delete Google Drive Files**\n__Delete google drive files. Use /{BotCommands.Delete[0]} (File/Folder URL) to delete file or reply /{BotCommands.Delete[0]} to bot message.\nYou can also empty trash files use /{BotCommands.EmptyTrash[0]}\nNote: Files are deleted permanently. This process cannot be undone.\n\n**Copy Google Drive Files**\n__Yes, Clone or Copy Google Drive Files.\n__Use /{BotCommands.Clone[0]} (File id / Folder id or URL) to copy Google Drive Files in your Google Drive Account.__",
        
        "**Rules & Precautions**\n__1. Don't copy BIG Google Drive Files/Folders. It may hang the bot and your files maybe damaged.\n2. Send One request at a time unless bot will stop all processes.\n3. Don't send slow links @transload it first.\n4. Don't misuse, overload or abuse this free service.__",
        
        # Dont remove this ↓ if you respect developer.
        "**Developed by @viperadnan**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **හානවද යකෝ ඔච්චර 😬.**\n__ටිකකින් වරෙන්😬.__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **එහම පයිල්/ෆෝල්ඩර් එකක් නෑ😔.**\n__File id - {} Not found. Make sure it\'s exists and accessible by the logged account.__"
    
    INVALID_GDRIVE_URL = "❗ **Gdrive ලින්ක් එක වැරදී☹️**\nහරි ලින්ක් එකක් දාපන්😬."
    
    COPIED_SUCCESSFULLY = "✅ **හරි බඩු කොපි උනා.**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **Gdrive එකට කනෙක්ට් කරපන් 😏.**\n__Send /{BotCommands.Authorize[0]} to authenticate.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **ඩවුන් උනා✅ බඩු අප්ලෝඩ් වෙනෝ😁...**\n**Filename:** ```{}```\n**Size:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **බඩු අප්ලෝඩ් වුනා එහෙනම් කොල්ලෝ අපි ගියා🙋.**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**Failed පම්කක් 😐 ආයේ දාහන්**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **බඩු ඩවුන් වෙනෝ😁...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **මෙයා මේ පම්ක්ක ඔබලා😂 Gdrive එකට කනෙක්ට් වෙලා ඉන්නේ.**\n__Use /revoke Gdrive එකෙන්  මං අයින් කරන්න.__\n__ලින්ක්/telegram file දාම්පන් 📤  Google Drive අප්ලෝඩ් කරන්න__"
    
    FLOW_IS_NONE = f"❗ **Invalid Code පම්කක්**\n__Run {BotCommands.Authorize[0]} first.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Gdrive එකට කනෙක්ට්  උනා✅.**'
    
    INVALID_AUTH_CODE = '❗ **Invalid Code ටෝකන් වැඩ නෑ**\n__ටෝකන් එක හරියට එවහන් යකෝ😐. ආයේ Gdrive එකට කනෙක්ට් කරන්න Authorization URL__'
    
    AUTH_TEXT = "⛓️ **Gdrive එකට කනෙක්ට් කරන්න ඔය ලින්ක් එකෙන් ලොග්වෙන්න [URL]({}) Succes code එක කොපි කරලා මට එවන්න.**\n__ලින්ක එකට යන්න URL > Allow permissions දාපන් >Code එක ගන්න > Succes code එක කොපි කරලා මට එවන්න__"
    
    DOWNLOAD_TG_FILE = "📥 **බඩු ඩවුන් වෙනෝ😌...**\n**Filename:** ```{}```\n**Size:** ```{}```\n**MimeType:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **ඩවුන් වෙන ෆෝල්ඩර් එක සෙට් උනා.**\n__Your custom folder id - {}\nUse__ ```/{} clear``` __to clear it.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **ඩවුන් වෙන ෆෝල්ඩර් එක අයින් කරා.**\n__Use__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __to set it back__.'
    
    CURRENT_PARENT = "🆔 **ඩවුන් වෙන ෆෝල්ඩර් එක ID - {}**\n__Use__ ```/{} (Folder link)``` __to change it.__"
    
    REVOKED = f"🔓 **Gdrive එකෙන්  මං අයින් වෙනෝ එහනම් කොල්ලෝ අපි ගියා🙋.**\n__Use /{BotCommands.Authorize[0]} ආයේ Gdrive එකට කනෙක්ට් කරන්න.__"
    
    NOT_FOLDER_LINK = "❗ **Gdrive folder ලින්ක් එක වැරදී😐.**\n__හරි ෆෝල්ඩර් ලින්ක් එකක් දාපන්😬.__"
    
    CLONING = "🗂️ **බඩු ක්ලෝන් වෙනෝ...**\n__G-Drive Link - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ Gdrive ලින්ක් එක වැරදී😐.**\n__Usage - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "❗ **ඇකස්ස් නෑ  පයිල් එකට 😒.**\n__File id - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **බඩු අයින් කරා.**\n__File deleted permanently !\nFile id - {}__"
    
    WENT_WRONG = "⁉️ **ERROR: මෙයා මේ පම්ක්ක ඔබලා  ආයේ දාහන් ටිකකින්**\n__Please try again later.__"
    
    EMPTY_TRASH = "🗑️🚮**බඩු අයිම් කරා !**"
    
    PROVIDE_YTDL_LINK = "❗**Provide a valid YouTube-DL supported link.**"
