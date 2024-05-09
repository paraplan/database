CREATE MIGRATION m1ekih3afdm4oskyphvihip2tpbiuuhyw6tcrjkl6lxqm74s47awlq
    ONTO initial
{
  CREATE TYPE default::Cabinet {
      CREATE REQUIRED PROPERTY name: std::str;
      CREATE REQUIRED PROPERTY room: std::str;
  };
  CREATE TYPE default::SubGroupHour {
      CREATE REQUIRED LINK cabinet: default::Cabinet;
      CREATE REQUIRED PROPERTY occupation: std::str;
  };
  CREATE TYPE default::`Group` {
      CREATE REQUIRED PROPERTY full_name: std::str;
      CREATE REQUIRED PROPERTY name: std::str;
  };
  CREATE TYPE default::Hour {
      CREATE REQUIRED MULTI LINK sub_groups: default::SubGroupHour;
  };
  CREATE TYPE default::StudyDay {
      CREATE REQUIRED LINK `group`: default::`Group`;
      CREATE REQUIRED MULTI LINK hours: default::Hour;
      CREATE REQUIRED PROPERTY date: std::datetime;
  };
  CREATE TYPE default::User {
      CREATE LINK `group`: default::`Group`;
      CREATE REQUIRED PROPERTY created_at: std::datetime {
          SET default := (std::datetime_of_transaction());
          SET readonly := true;
      };
      CREATE REQUIRED PROPERTY telegram_id: std::int64 {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
