drop table if exists refcards;
    create table refcards (
        id integer primary key autoincrement,
        context text not null,
        refcard text not null
);