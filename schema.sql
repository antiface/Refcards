drop table if exists refcards;
    create table refcards (
        id integer primary key autoincrement,
        created_at DATETIME DEFAULT (STRFTIME('%d-%m-%Y   %H:%M:%S', 'NOW','localtime')),
        context text not null,
        refcard text not null
);
