CREATE MIGRATION m1eeajflnf4vddocsiisquirvoydhutaizucaxullorv5yowlgso5q
    ONTO m1vxi53gj7tvjeixcaqqa7oc75hgkqac45d3hwndzq7y7vsy7eezma
{
  ALTER TYPE default::`Group` {
      CREATE CONSTRAINT std::exclusive ON ((.name, .full_name));
  };
};
