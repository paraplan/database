CREATE MIGRATION m1m2k4glih5ot34ebp3nbzglkv4zwcb6reempfqwqihcunbieiq7zq
    ONTO m1q3l2gp74djmkfbxw6orvcj4a5qmugdr5zmpzvs67qkhgrygx6owa
{
  ALTER TYPE default::Hour {
      CREATE REQUIRED PROPERTY number: std::int16 {
          SET REQUIRED USING (<std::int16>{1});
      };
  };
};
