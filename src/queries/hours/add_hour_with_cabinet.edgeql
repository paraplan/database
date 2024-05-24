with cabinet := (
  insert Cabinet {
    number := <str>$cabinet_number,
    details := <str>$cabinet_details
  } unless conflict on .number else Cabinet
)

insert Hour {
  sub_group := <int16>$sub_group,
  occupation := <str>$occupation,
  cabinet := cabinet,
} unless conflict on (.occupation, .cabinet, .sub_group) else Hour;
