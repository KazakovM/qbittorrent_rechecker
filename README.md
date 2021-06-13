# qbittorrent_rechecker

Скрипт для запуска принудительной проверки зависших торрентов в qbittorrent. 

Зависший торрент - торрент в статусе "Stalled" и прогрессом более 99%.

_Группа в Telegram: https://t.me/btt_automation_

## Настройка скрипта
1. Скачать и устанавить [Python](https://www.python.org/downloads/) последней версии. При установке обязательно добавить запись в **PATH**.
2. Скачать данный репозиторий через **git** или архив (_Code_ -> _Download ZIP_).
3. Открыть настройки **qbittorrent** -> _Веб-интерфейс_ -> поставить галочку _"Веб-интерфейс (удаленное управление)"_.
4. Задать порт (уникальный, не совпадающий с другим клиентом), логин, пароль.
5. Указать хост, порт, логин, пароль в файле **config.json**.
6. Запустить файл **INSTALL.bat** для установки необходимых модулей (только один раз).
7. Запустить файл **START.bat**.

### _Donate:_
* TRX/BTT: TEyaTpdKMCiKyQsokb89oBoLEiyzU1KHRE
* RUB: [qiwi.com/n/PAIDE724](QIWI)

### _Протестированные VPS_:
* [cp.zomro.com](https://zomro.com/?from=296803)
* [vultr.com](https://www.vultr.com/?ref=8883507)
* [macloud.ru](https://macloud.ru/?partner=qby7f922cx)
