-- Single variable yes/no
main = do
  x <- getLine
  putStrLn $ if solve x then "Heisei" else "TBD"

solve :: String -> Bool
solve s =
  let m = fst $ splitAt 2 $ snd $ splitAt 5 s
  in if read m <= 4 then True else False
