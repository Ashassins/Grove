<div class="container col-lg-12">
    <br>
    <div class="our-bg p-1 rounded shadow-xl container sm:max-w-lg sm:rounded-lg">
        <div style="">
            <h1 class="text-center text-2xl font-light font-serif">
                {treeNameFromID(treeID)}'s Tree
            </h1>
            <p class="text-center font-serif">Planted: DATE</p>
            <p class="text-center font-serif">{treeStatusFromID(treeID)}</p>
        </div>
        <span class="container"> 
            <img style="max-width: 25rem" class="container-fluid" src="/stage3.png" alt="Tree">
        </span>
        <br>
        <p class="flex justify-center font-serif text-s">250/500 xp to lvl 4</p>
        <div class="flex justify-center">
            <div class="w-full bg-gray-200 h-2 mb-6" style="max-width: 25rem">
                <div class="bg-green-500 h-2" style="width: 50%">
                </div>
            </div>
        </div>
        <div class="flex justify-center">
            <div style="columns-3 md:columns-3">
                <div>
                    {#if treeID > 1}
                        <a href="/tree?treeID={treeID - 1}"><img class="max-h-10" src="/black-chevron-left.png"></a>
                    {/if}
                </div>
                <div>
                    <button type="submit" style="background-color: #19783C !important; border-color: #19783C!important" aria-disabled="false" class="btn btn-lg btn-success active">Shake</button>
                </div>
                    <div>
                    {#if treeID < 3}
                        <a href="/tree?treeID={treeID + 1}"><img class="max-h-10"  src="/black-chevron-right.png"></a>
                    {/if}
                </div>
            </div>
        </div>
        <br>
        <p class="flex justify-center" style="display:none">You may shake again at TIME </p>
    </div>
    <div class="our-bg p-1 rounded shadow-xl container sm:max-w-lg sm:rounded-lg">
        <div class="mycards container-content sm:mx-auto  sm:px-10"> 
            <h1 class="flex justify-center text-3xl font-light font-serif">Daily Quests</h1>
            {#each dispQuests() as quest}
                <div id="questEntry" class="relative align-middle content-center">
                    <ul class=""> 
                        <label class="checkbox path">
                            <input type="checkbox">
                            <svg viewBox="0 0 21 21">
                                <path d="M5,10.75 L8.5,14.25 L19.4,2.3 C18.8333333,1.43333333 18.0333333,1 17,1 L4,1 C2.35,1 1,2.35 1,4 L1,17 C1,18.65 2.35,20 4,20 L17,20 C18.65,20 20,18.65 20,17 L20,7.99769186"></path>
                            </svg>
                        </label>
                        <span class="pb-3"> &nbsp;{quest.content}</span> 
                        <!-- I GIVE UP ON SPACING -->
                    </ul>
                </div>
            {/each}
        </div>
        <div class="content-center justify-center flex">
            <button type="button submit" style="background-color: #F8E58E !important; border-color: #F8E58E!important" aria-disabled="false" class="btn btn-lg btn-warning active">Good Morning!</button>
            &nbsp;&nbsp;&nbsp;&nbsp;
            <button type="button submit" style="background-color: #7C90DB !important; border-color: #7C90DB!important" aria-disabled="false" class="btn  btn-lg btn-primary active">&nbsp;&nbsp;Good Night!&nbsp;&nbsp;</button>
        </div>
        <br>
    </div>
    <br>
    <div id="treeSettingsCard" class="our-bg p-1 rounded shadow-xl container sm:max-w-lg sm:rounded-lg">
        <div class="mycards container-content sm:mx-auto sm:px-10"> 
            <h1 class="flex justify-center text-3xl font-light font-serif">Settings</h1>
            <div class="form-check form-switch">
                <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchNotifs" checked>
                <label class="form-check-label" for="flexSwitchNotifs">Get Notifications</label>
            </div>
            <div class="form-check form-switch">
                <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchRomantic" checked>
                <label class="form-check-label" for="flexSwitchRomantic">This is a Romantic Relationship</label>
            </div>
            <a href="/wishlist?treeID={treeID}" class="text-center font-serif">View {treeNameFromID(treeID)}'s Wishlist</a>
        </div>
    </div>
    <br>
</div>

<script>
    import { page } from '$app/stores';
    const treeID = parseInt($page.url.searchParams.get('treeID'), 10);

    let trees = [
        { treeID: 1, name: "Ramune", status: "Happy b/c sushi"},
        { treeID: 2, name: "Fanta", status: "Missing my GF hours"},
        { treeID: 3, name: "Ros??", status: "It's a wine kind of night" },
    ]

    let quests = [
        { dateTime: 1674939694, content: "Take a pic of a pet", status: "active" },
        { dateTime: 1674939695, content: "Whatcha Eating?", status: "active" },
        { dateTime: 1674939696, content: "Something Funny", status: "active" },
        { dateTime: 1674939696, content: "Whatcha Doing?", status: "inactive" },
    ]

    function dispQuests() {
        return quests.filter(function (el)
        {
            return el.status === "active";
        }
        );
    }

    function treeNameFromID(id) {
        return trees.filter(obj => {
            return obj.treeID === id
        })[0].name
    }

    function treeStatusFromID(id) {
        return trees.filter(obj => {
            return obj.treeID === id
        })[0].status
    }
    // console.log(dispNotis());
</script>

<style lang="postcss">
    .mycards {
		margin: 1.5rem;
    }
    .checkbox {
    --background: #fff;
    --border: #D1D6EE;
    --border-hover: #BBC1E1;
    --border-active: #1E2235;
    --tick: #fff;
    position: relative;
    input,
    svg {
        width: 21px;
        height: 21px;
        display: flex;
    }
    input {
        -webkit-appearance: none;
        -moz-appearance: none;
        position: relative;
        outline: none;
        background: var(--background);
        border: none;
        margin: 0;
        padding: 0;
        cursor: pointer;
        border-radius: 4px;
        transition: box-shadow .3s;
        box-shadow: inset 0 0 0 var(--s, 1px) var(--b, var(--border));
        &:hover {
            --s: 2px;
            --b: var(--border-hover);
        }
        &:checked {
            --b: var(--border-active);
        }
    }
    svg {
        pointer-events: none;
        fill: none;
        stroke-width: 2px;
        stroke-linecap: round;
        stroke-linejoin: round;
        stroke: var(--stroke, var(--border-active));
        position: absolute;
        top: 0;
        left: 0;
        width: 21px;
        height: 21px;
        transform: scale(var(--scale, 1)) translateZ(0);
    }
    &.path {
        input {
            &:checked {
                --s: 2px;
                transition-delay: .4s;
                & + svg {
                    --a: 16.1 86.12;
                    --o: 102.22;
                }
            }
        }
        svg {
            stroke-dasharray: var(--a, 86.12);
            stroke-dashoffset: var(--o, 86.12);
            transition: stroke-dasharray .6s, stroke-dashoffset .6s;
        }
    }
}
</style>