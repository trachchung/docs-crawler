<!-- Source: https://docs.meshconnect.com/advanced/language -->

[Skip to main content](https://docs.meshconnect.com/advanced/language#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Advanced
Enabling Multi-Language Support for Link
##### Get Started


##### Advanced
  * [Best UX Practices & Examples](https://docs.meshconnect.com/advanced/best-ux-practices)
  * [Configuring Transfer Options](https://docs.meshconnect.com/advanced/configuring-transfer-options)
  * [Mesh Managed Tokens (MMT)](https://docs.meshconnect.com/advanced/mesh-managed-tokens)
  * [Intelligent Provider Filtering in Mesh Link](https://docs.meshconnect.com/advanced/intelligent-provider-filtering)
  * [Enabling Multi-Language Support for Link](https://docs.meshconnect.com/advanced/language)
  * [Verifying Self-Hosted Wallets](https://docs.meshconnect.com/advanced/verifying-self-hosted-wallets)
  * [Managing Sub-Clients](https://docs.meshconnect.com/advanced/sub-client-branding)
  * [Mesh Link SDK Events](https://docs.meshconnect.com/advanced/link-ui-events)
  * [Foreign Currency Support](https://docs.meshconnect.com/advanced/foreign-currency-support)


##### Testing
  * Sandbox
  * [Troubleshooting link](https://docs.meshconnect.com/testing/troubleshooting-link)
  * [Transfer Webhooks](https://docs.meshconnect.com/testing/webhooks)


#  🔎 Overview
This guide explains how to configure Link (the Mesh SDK) to support multiple languages for a localized user experience. The `language` parameter allows you to automatically match the user’s device/browser language, or specify a particular language and locale.
#  ⚙️ Possible Values
  * `<BCP 47 code>`: A specific language code enumerated as the 2 digit language identifier (eg. “`fr`” for French) and the 2 digit region identifier (eg. “`CA`” for Canada), combined as “`fr-CA`”. Alternatively, the SDK will accept an input of only the language (eg. “`fr`”).
  * If the indicated language (eg. “`fr`”) is followed by a region code (eg. “`CA`”) that is not recognized or supported for that language, Link will fall back to the default translation for that language, if available (eg. “`fr-FR`”). If no translation for the language is available, Link will default to “`en-US`” (English, US).
  * If you do not provide a value for the parameter, or if you provide a value for a language that is not supported, Link will default to “`en-US`” (English, US).
  * `system`: Link will detect the default language on the user’s browser and/or device and display Link in that language. If it is an unsupported value, it will fallback to another locale for that language, or it will fallback to the global default of `en-US`.


#  **🛠️ Implementation**
##  **1. Initialize Link with`language`**
When you initialize Link in your application, use the `language` parameter to specify the desired language behavior.
###  🌐 Web SDK example

```
const connection = createLink({
  ...
  language: 'system',
  ...
})

```

###  🍏 iOS Native SDK example

```
let settings = LinkSettings(language: "system",
                            ...)

```

###  🤖 Android Native SDK example

```
val configuration = LinkConfiguration(
  ...
  language = "system",
  ...


```

###  ReactNative SDK example

```
return <...
        settings={{
          language: 'system',
          ...
        }}

```

###  Flutter SDK example

```
final result = await MeshSdk.show(
  context,
  configuration: MeshConfiguration(
    language: 'system',
    ...
      ),

```

##  **2. Test your implementation**
Thoroughly test your implementation to ensure a seamless experience for your users:
  * Verify that Link displays correctly in the languages you intend to support.
  * Please let your Mesh representative know if you spot any incorrectly translated words or phrases, or any layout issues (for example with right-to-left or character-based languages).


#  Currently supported languages  
| **Status**  | **Language**  | **Region**  | **Locale code**  |  
| --- | --- | --- | --- |  
| **live**  | English  | United States **global default**  | **`en-US`** |  
| **live**  | Spanish  | United States **es default**  | **`es-US`** |  
| **live**  | Russian  | Russia  | **`ru-RU`** |  
| **live**  | French  | France **fr default**  | **`fr-FR`** |  
| **live**  | Chinese/Mandarin (Simplified)  | China **zh default**  | **`zh-CN`** |  
| **live**  | Turkish  | Turkey  | **`tr-TR`** |  
| **live**  | Polish  | Poland  | **`pl-PL`** |  
| **live**  | Japanese  | Japan  | **`ja-JP`** |  
| **live**  | German  | Germany  | **`de-DE`** |  
| **live**  | Finnish  | Finland  | **`fi-FI`** |  
| **live**  | Hindi  | India  | **`hi-IN`** |  
| **live**  | Indonesian  | Indonesia  | **`id-ID`** |  
| **live**  | Malay  | Malaysia  | `ms-MS`  |  
| **live**  | Portuguese  | Portugal **pt default**  | **`pt-PT`** |  
| **live**  | Thai  | Thailand  | **`th-TH`** |  
| **live**  | Ukrainian  | Ukraine  | `uk-UK`  |  
| **live**  | Uzbek  | Uzbekistan  | `uz-UZ`  |  
| **live**  | Vietnamese  | Vietnam  | **`vi-VN`** |  
| **live**  | system  | **`system`** |  
| **backlog**  | Arabic  | Egypt  | **`ar-EG`** |  
| **backlog**  | Chinese/Mandarin (Traditional)  | United States  | **`zh-US`** |  
| **backlog**  | Chinese  | Hong Kong  | **`zh-HK`** |  
| **backlog**  | Chinese  | Taiwan  | **`zh-TW`** |  
| **backlog**  | Czech  | Czech Republic  | **`cs-CZ`** |  
| **backlog**  | Danish  | Denmark  | **`da-DK`** |  
| **backlog**  | Dutch, Flemish  | Belgium  | **`nl-NL`** |  
| **backlog**  | English  | Australia  | **`en-AU`** |  
| **backlog**  | English  | India  | **`en-IN`** |  
| **backlog**  | English  | United Kingdom  | **`en-GB`** |  
| **backlog**  | French  | Canada  | **`fr-CA`** |  
| **backlog**  | Greek, Modern (1453–)  | Greece  | **`el-GR`** |  
| **backlog**  | Hebrew  | Israel  | **`he-IL`** |  
| **backlog**  | Hungarian  | Hungary  | **`hu-HU`** |  
| **backlog**  | Italian  | Italy  | **`it-IT`** |  
| **backlog**  | Korean  | South Korea  | **`ko-KR`** |  
| **backlog**  | Norwegian  | Norway  | **`no-NO`** |  
| **backlog**  | Portuguese  | Brazil  | **`pt-BR`** |  
| **backlog**  | Slovak  | Slovakia  | **`sk-SK`** |  
| **backlog**  | Spanish, Castilian  | Spain  | **`es-ES`** |  
| **backlog**  | Swedish  | Sweden  | **`sv-SE`** |  
Was this page helpful?
YesNo
[ Intelligent Provider Filtering in Mesh Link Previous ](https://docs.meshconnect.com/advanced/intelligent-provider-filtering)[ Paylinks Next ](https://docs.meshconnect.com/advanced/paylinks)
Ctrl+I
On this page
  * [⚙️ Possible Values](https://docs.meshconnect.com/advanced/language#-possible-values)
  * [🛠️ Implementation](https://docs.meshconnect.com/advanced/language#-implementation)
  * [1. Initialize Link with language](https://docs.meshconnect.com/advanced/language#1-initialize-link-with-language)
  * [🌐 Web SDK example](https://docs.meshconnect.com/advanced/language#-web-sdk-example)
  * [🍏 iOS Native SDK example](https://docs.meshconnect.com/advanced/language#-ios-native-sdk-example)
  * [🤖 Android Native SDK example](https://docs.meshconnect.com/advanced/language#-android-native-sdk-example)
  * [ReactNative SDK example](https://docs.meshconnect.com/advanced/language#reactnative-sdk-example)
  * [Flutter SDK example](https://docs.meshconnect.com/advanced/language#flutter-sdk-example)
  * [2. Test your implementation](https://docs.meshconnect.com/advanced/language#2-test-your-implementation)
  * [Currently supported languages](https://docs.meshconnect.com/advanced/language#currently-supported-languages)


Assistant
Responses are generated using AI and may contain mistakes.
