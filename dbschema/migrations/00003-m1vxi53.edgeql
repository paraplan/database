CREATE MIGRATION m1vxi53gj7tvjeixcaqqa7oc75hgkqac45d3hwndzq7y7vsy7eezma
    ONTO m1wvtrjbfl5gon4rphblhhdxo2phbczjqevmtkdsfmtkezg2zijjpa
{
  ALTER TYPE default::Cabinet {
      ALTER PROPERTY name {
          RENAME TO details;
      };
  };
  ALTER TYPE default::Cabinet {
      ALTER PROPERTY room {
          RENAME TO number;
      };
  };
  ALTER TYPE default::Hour {
      CREATE LINK cabinet: default::Cabinet;
  };
  ALTER TYPE default::Hour {
      CREATE REQUIRED PROPERTY occupation: std::str {
          SET REQUIRED USING (<std::str>{''});
      };
  };
  ALTER TYPE default::Hour {
      CREATE REQUIRED PROPERTY sub_group: std::int16 {
          SET REQUIRED USING (<std::int16>{1});
      };
      CREATE CONSTRAINT std::exclusive ON ((.cabinet, .occupation, .sub_group));
  };
  ALTER TYPE default::Hour {
      DROP LINK sub_groups;
  };
  DROP TYPE default::SubGroupHour;
};
