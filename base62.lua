local M = {}

function char(num)
    if 0 <= num and num <= 9 then
        return tostring(num)
    elseif 10 <= num and num <= 35 then
        return string.char(num + 55)
    elseif 36 <= num and num <= 61 then
        return string.char(num + 61)
    end
end

function gen_list(num, temp_list)
    if num >= 62 then
        character = char(num%62)
        table.insert(temp_list, 1, character)
        return gen_list(math.floor(num/62), temp_list)
    elseif 0 <= num and num <= 61 then
        character = char(num)
        table.insert(temp_list, 1, character)
        return temp_list
    end
end

function M.encode(num)
    local temp_list = gen_list(num, {})
    return table.concat(temp_list, "")
end

return M
