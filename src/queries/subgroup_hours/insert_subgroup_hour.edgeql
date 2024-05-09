insert SubGroupHour {
  cabinet := (select Cabinet filter .id = <uuid>$cabinet_id),
  occupation := <str>$occupation
};
