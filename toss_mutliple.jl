begin
	using StatsBase
	function coin_toss(n)
		toss = []
		head = 0
		for i in 1:n
			push!(toss, sample(["H", "T"], 1, replace = false))
		end
		for i in toss
			if i == ["H"]
				head += 1
			end
		end
		return head/n
	end
end
