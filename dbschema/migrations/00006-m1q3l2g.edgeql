CREATE MIGRATION m1q3l2gp74djmkfbxw6orvcj4a5qmugdr5zmpzvs67qkhgrygx6owa
    ONTO m1manibntpfnyz3256c5zqzvlw7od5m6vrlmlwnlemu7cfw2wmwrja
{
  ALTER TYPE default::Hour {
      DROP CONSTRAINT std::exclusive ON ((.cabinet, .occupation, .sub_group));
  };
};
