# qbittorrent_rechecker

Скрипт для докачивания зависших торрентов и удаления по критерию размера.


[Группа в Telegram](https://t.me/joinchat/Jsb2S7JnaFhlY2Qy)

## Настройка скрипта
1. Скачать и устанавить [Python](https://www.python.org/downloads/) последней версии. При установке обязательно добавить запись в **PATH**.
2. Скачать данный репозиторий через **git** или архив (_Code_ -> _Download ZIP_).
3. Открыть настройки **qbittorrent** -> _Веб-интерфейс_ -> поставить галочку _"Веб-интерфейс (удаленное управление)"_.
4. Задать порт (уникальный, не совпадающий с другим клиентом), логин, пароль.
5. Указать хост, порт, логин, пароль в файле **config.json**.
6. Указать минимальный и максимальный размер торрента (гб) в **config.json** (0 и 100000 если удаление не требуется).
7. Запустить файл **INSTALL.bat** для установки необходимых модулей (только один раз).
8. Запустить файл **START.bat**.

### _Donate:_
* TRX/BTT: TEyaTpdKMCiKyQsokb89oBoLEiyzU1KHRE
* RUB: [qiwi.com/n/PAIDE724](QIWI)

### _Протестированные VPS_:
* [cp.zomro.com](https://zomro.com/?from=296803)
* [vultr.com](https://www.vultr.com/?ref=8883507) - принимает не все карты. Нормально работает с [Tinkoff](https://www.tinkoff.ru/sl/2HFYdv2GfO6) - по [ссылке](https://www.tinkoff.ru/sl/2HFYdv2GfO6) карта с бесплатным обслуживанием.
* [macloud.ru](https://macloud.ru/?partner=21x4zp5121)
