-- Single variable
main = do
  x <- getLine
  putStrLn . show $ solve x

solve :: String -> Int
solve xs =
  let n0 = length $ filter (\x -> x == '0') xs
      n1 = length $ filter (\x -> x == '1') xs
  in (length xs) - (abs (n0 - n1))
