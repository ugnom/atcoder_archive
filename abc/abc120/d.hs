-- Multi lines of lists
import Data.Traversable
import Data.List as L
import Data.Set as S

main = do
  (n:m:xs) <- L.map read . words <$> getLine
  ps <- for [1..m] $ \x -> do
    (\(x:y:ys) -> (x,y)) . L.map (read::String->Int) . words <$> getLine
  putStrLn . unlines . L.map show  $ solve ps n

--solve :: [(Int,Int)] -> [Int]
solve ps n =
  let revps = reverse ps
      calcn = calc n
  in tail $ reverse $ L.map ((\x -> calcn - x) . sum . (L.map (calc . size))) $ scanl (\s t -> solve1 t s [] []) [] revps

calc x = (x * (x - 1)) `div` 2

solve1 (a,b) [] curSets [] =
  (fromList [a,b]):curSets
solve1 (a,b) [] curSets newSets =
  (unions newSets):curSets
solve1 (a,b) all@(set:sets) curSets newSets =
  let am = a `member` set
      bm = b `member` set
  in if am && bm then
    solve1 (a,b) [] curSets (set:newSets)
  else if am then
    solve1 (a,b) sets  curSets ((S.insert b set):newSets)
  else if bm then
    solve1 (a,b) sets  curSets ((S.insert a set):newSets)
  else
    solve1 (a,b) sets (set:curSets) newSets
