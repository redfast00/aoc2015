import Data.Maybe

main = do
    content <- readFile "input"
    print $ getVerdiep content
    print $ whenBasement content

offset :: Char -> Int
offset '(' = 1
offset ')' = -1

getVerdiep :: String -> Int
getVerdiep [] = 0
getVerdiep (x:xs) = getVerdiep xs + offset x


whenBasement :: String -> Maybe Int
whenBasement input = snd <$> listToMaybe underground
    where offsets = cumsum 0 (map offset input)
          underground = filter (\x -> fst x < 0) (zip offsets [1..])

cumsum :: Int -> [Int] -> [Int]
cumsum _ [] = []
cumsum acc (x:xs) = acc + x: cumsum (x + acc) xs
