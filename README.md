# bitrix_app
Bitrix24 application 
Данный скрипт раз в час обращается к API Битрикс24 и упаковывает полученные данные в файл bitrix_data.xlsx
## Перед началом работы
Перед началом работы необхадимо установить(если ещё не установлены) некоторые библиотеки :
```
 fast_bitrix24
 pandas
 XlsxWriter
```

Также необходимо в той директории, в которой будет расположен скрипт разместить файл 	**webhook.txt**, в котором будет Ваш вебхук.
Помимо этого, в том разделе, где генерируется вебхук, необходимо в графе **Настройки прав** добавить правва доступа к CRM 
