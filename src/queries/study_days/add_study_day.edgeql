with
  `group` := (
    insert `Group` {
      full_name := <str>$group_full_name,
      name := <str>$group_name
    } unless conflict on (.full_name, .name) else `Group`
  ),
  hours := (
    select Hour filter .id in array_unpack(<array<uuid>>$hour_ids)
  )

insert StudyDay {
  `group` := `group`,
  hours := hours,
  date := <datetime>$date
} unless conflict on (.`group`, .date) else StudyDay;
