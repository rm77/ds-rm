---- MODULE jam ----
EXTENDS Integers, Sequences, TLC

(*--algorithm dup
  variable seq = <<1, 2, 3, 4,5,6,7,7,8>>;
  index = 1;
  seen = {};
  is_unique = TRUE;

begin
  Iterate:
    while index <= Len(seq) do
      print seq[index];
      if seq[index] \notin seen then
        seen := seen \union {seq[index]};
      else
        is_unique := FALSE;
        skip
      end if;
      index := index + 1;
    end while;
  Selesai:
    print is_unique;
end algorithm; *)
====
