main = do
  s <- getLine
  t <- getLine
  case solve s t of
    Nothing -> do
      putStrLn "UNRESTORABLE"
    Just u -> do
      putStrLn u

solve :: String -> String -> Maybe String
solve [] t = Nothing
solve s t =
  let this = if fit s t then Just (map (\x -> if x == '?' then 'a' else x) (t ++ (drop (length t) s))) else Nothing
      si = if head s == '?' then 'a' else head s
  in case solve (tail s) t of
    Just u -> case this of
      Nothing -> Just (si:u)
      Just r -> Just (min r (si:u))
    Nothing -> this

fit :: String -> String -> Bool
fit [] [] = True
fit (x:xs) [] = True
fit [] (x:xs) = False
fit (si:s) (ti:t) = if si == '?' || si == ti then fit s t else False
