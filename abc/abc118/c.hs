main = do
  x <- getLine
  ps <- map read . words <$> getLine
  putStrLn . show $ solve ps

solve :: [Integer] -> Integer
solve ps =
  let mi = minimum ps
      calced = filter (/= 0) . map (\x -> x `mod` mi) $ ps
  in if null calced then mi else solve (mi:calced)
