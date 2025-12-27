#=================== Load Package ====================
library(stringr)

#=================== Detect & Locate ====================
str_detect(string, pattern)
str_starts(string, pattern)
str_which(string, pattern)
str_locate(string, pattern)
str_count(string, pattern)

#=================== Subset & Extract ====================
str_sub(string, start = 1, end = -1)
str_subset(string, pattern)
str_extract(string, pattern)
str_match(string, pattern)

#=================== Modify Strings ====================
str_sub(string, 1, 3) <- "abc"
str_replace(string, pattern, replacement)
str_replace_all(string, pattern, replacement)

#=================== Case Conversion ====================
str_to_lower(string)
str_to_upper(string)
str_to_title(string)

#=================== Join & Split ====================
str_dup(string, n)
str_split_fixed(string, pattern, n)