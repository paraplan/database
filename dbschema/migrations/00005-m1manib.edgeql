CREATE MIGRATION m1manibntpfnyz3256c5zqzvlw7od5m6vrlmlwnlemu7cfw2wmwrja
    ONTO m1eeajflnf4vddocsiisquirvoydhutaizucaxullorv5yowlgso5q
{
  ALTER TYPE default::StudyDay {
      CREATE CONSTRAINT std::exclusive ON ((.`group`, .date));
  };
};
