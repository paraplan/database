insert StudyDay {
  date := <datetime>$date,
  `group` := ( select `Group` filter .id = <uuid>$group_id ),
  hours := (
    select Hour
    filter .id in array_unpack(<array<uuid>>$hour_ids)
  ),
}
