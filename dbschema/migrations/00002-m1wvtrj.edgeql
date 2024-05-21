CREATE MIGRATION m1wvtrjbfl5gon4rphblhhdxo2phbczjqevmtkdsfmtkezg2zijjpa
    ONTO m1ekih3afdm4oskyphvihip2tpbiuuhyw6tcrjkl6lxqm74s47awlq
{
  ALTER TYPE default::Cabinet {
      ALTER PROPERTY room {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
