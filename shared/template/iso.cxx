/*---------- begin exec-head.in ----------*/
/*! \file iso.cxx
 *
 * Generated from iso.diderot.
 *
 * Command: /Users/chariseechiw/diderot/vis15/bin/diderotc --exec iso.diderot
 * Version: vis15:2016-07-29
 */
/*---------- end exec-head.in ----------*/

#define DIDEROT_HAS_STRAND_DIE
#define DIDEROT_HAS_KILL_ALL
/*---------- begin exec-incl.in ----------*/
#define DIDEROT_STANDALONE_EXEC
#define DIDEROT_SINGLE_PRECISION
#define DIDEROT_INT
#define DIDEROT_TARGET_SEQUENTIAL
#include "diderot/diderot.hxx"
/*---------- end exec-incl.in ----------*/

// ***** Begin synthesized types *****

namespace Diderot {
    typedef float vec2 __attribute__ ((vector_size (8)));
    typedef float vec6 __attribute__ ((vector_size (32)));
    struct tensor_ref_2 : public diderot::tensor_ref<float,2> {
        tensor_ref_2 (const float *src);
        tensor_ref_2 (struct tensor_2 const & ten);
        tensor_ref_2 (tensor_ref_2 const & ten);
    };
    struct tensor_ref_2_2 : public diderot::tensor_ref<float,4> {
        tensor_ref_2_2 (const float *src);
        tensor_ref_2_2 (struct tensor_2_2 const & ten);
        tensor_ref_2_2 (tensor_ref_2_2 const & ten);
        tensor_ref_2 last (uint32_t i)
        {
            return &this->_data[i];
        }
    };
    struct tensor_2 : public diderot::tensor<float,2> {
        tensor_2 ()
            : diderot::tensor<float,2>()
        { }
        tensor_2 (std::initializer_list< float > const & il)
            : diderot::tensor<float,2>(il)
        { }
        tensor_2 (const float *src)
            : diderot::tensor<float,2>(src)
        { }
        tensor_2 (tensor_2 const & ten)
            : diderot::tensor<float,2>(ten._data)
        { }
        ~tensor_2 () { }
        tensor_2 & operator= (tensor_2 const & src);
        tensor_2 & operator= (tensor_ref_2 const & src);
        tensor_2 & operator= (std::initializer_list< float > const & il);
        tensor_2 & operator= (const float *src);
    };
    struct tensor_2_2 : public diderot::tensor<float,4> {
        tensor_2_2 ()
            : diderot::tensor<float,4>()
        { }
        tensor_2_2 (std::initializer_list< float > const & il)
            : diderot::tensor<float,4>(il)
        { }
        tensor_2_2 (const float *src)
            : diderot::tensor<float,4>(src)
        { }
        tensor_2_2 (tensor_2_2 const & ten)
            : diderot::tensor<float,4>(ten._data)
        { }
        ~tensor_2_2 () { }
        tensor_2_2 & operator= (tensor_2_2 const & src);
        tensor_2_2 & operator= (tensor_ref_2_2 const & src);
        tensor_2_2 & operator= (std::initializer_list< float > const & il);
        tensor_2_2 & operator= (const float *src);
        tensor_ref_2 last (uint32_t i)
        {
            return &this->_data[i];
        }
    };
    inline tensor_ref_2::tensor_ref_2 (const float *src)
        : diderot::tensor_ref<float,2>(src)
    { }
    inline tensor_ref_2::tensor_ref_2 (struct tensor_2 const & ten)
        : diderot::tensor_ref<float,2>(ten._data)
    { }
    inline tensor_ref_2::tensor_ref_2 (tensor_ref_2 const & ten)
        : diderot::tensor_ref<float,2>(ten._data)
    { }
    inline tensor_ref_2_2::tensor_ref_2_2 (const float *src)
        : diderot::tensor_ref<float,4>(src)
    { }
    inline tensor_ref_2_2::tensor_ref_2_2 (struct tensor_2_2 const & ten)
        : diderot::tensor_ref<float,4>(ten._data)
    { }
    inline tensor_ref_2_2::tensor_ref_2_2 (tensor_ref_2_2 const & ten)
        : diderot::tensor_ref<float,4>(ten._data)
    { }
    inline tensor_2 & tensor_2::operator= (tensor_2 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_2 & tensor_2::operator= (tensor_ref_2 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_2 & tensor_2::operator= (std::initializer_list< float > const & il)
    {
        this->copy(il);
        return *this;
    }
    inline tensor_2 & tensor_2::operator= (const float *src)
    {
        this->copy(src);
        return *this;
    }
    inline tensor_2_2 & tensor_2_2::operator= (tensor_2_2 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_2_2 & tensor_2_2::operator= (tensor_ref_2_2 const & src)
    {
        this->copy(src._data);
        return *this;
    }
    inline tensor_2_2 & tensor_2_2::operator= (std::initializer_list< float > const & il)
    {
        this->copy(il);
        return *this;
    }
    inline tensor_2_2 & tensor_2_2::operator= (const float *src)
    {
        this->copy(src);
        return *this;
    }
} // namespace Diderot
// ***** End synthesized types *****

/*---------- begin namespace-open.in ----------*/
namespace Diderot {

static std::string ProgramName = "iso";

struct world;
struct iso_strand;
/*---------- end namespace-open.in ----------*/

/*---------- begin nrrd-save-helper.in ----------*/
/* helper function for saving output to nrrd file */
inline bool nrrd_save_helper (
        std::string const &stem,
        std::string const &suffix,
        std::string const &ext,
        Nrrd *nrrd)
{
    std::string file = stem + suffix + "." + ext;
    if (nrrdSave (file.c_str(), nrrd, nullptr)) {
        std::cerr << "Error saving \"" << file << "\":\n" << biffGetDone(NRRD) << std::endl;
        return true;
    }
    else {
        return false;
    }
}
/*---------- end nrrd-save-helper.in ----------*/

struct globals {
    float gv_isoval;
    int32_t gv_stepsMax;
    float gv_epsilon;
    diderot::image2d< float, float > gv_img;
    tensor_2 gv_cmin;
    tensor_2 gv_cmax;
    int32_t gv_size;
};
struct iso_strand {
    tensor_2 sv_pos;
    int32_t sv_steps;
};
/*---------- begin seq-sarr.in ----------*/
// forward declarations of strand methods
#ifdef DIDEROT_HAS_START_METHOD
static diderot::strand_status iso_start (iso_strand *self);
#endif // DIDEROT_HAS_START_METHOD
static diderot::strand_status iso_update (globals *glob, iso_strand *self);
#ifdef DIDEROT_HAS_STABILIZE_METHOD
static void iso_stabilize (iso_strand *self);
#endif // DIDEROT_HAS_STABILIZE_METHOD

// strand_array for SEQUENTIAL/NO BSP/SINGLE STATE/DIRECT ACCESS
//
struct strand_array {
    typedef iso_strand strand_t;
    typedef uint32_t index_t;
    typedef index_t sid_t;              // strand ID (index into strand-state storage)

    uint8_t             *_status;       // the array of status information for the strands
    char                *_storage;      // points to array of iso_strand structs
    uint32_t            _nItems;        // number of items in the _storage and _status arrays
    uint32_t            _nStable;       // number of stable strands
    uint32_t            _nActive;       // number of active strands
    uint32_t		_nFresh;	// number of fresh strands (new strands from create_strands)

    strand_array () : _status(nullptr), _storage(nullptr), _nItems(0) { }
    ~strand_array ();

    uint32_t in_state_index () const { return 0; /* dummy */ }

    uint32_t num_active () const { return this->_nActive; }
    uint32_t num_stable () const { return this->_nStable; }
    uint32_t num_alive () const { return this->_nActive+this->_nStable; }

  // return the ID of a strand, which is the same as the ix index
    sid_t id (index_t ix) const
    {
        assert (ix < this->_nItems);
        return ix;
    }
  // return a pointer to the strand with the given ID
    iso_strand *id_to_strand (sid_t id) const
    {
        assert (id < this->_nItems);
        return reinterpret_cast<iso_strand *>(this->_storage + id * sizeof(iso_strand));
    }

  // return a strand's status
    diderot::strand_status status (index_t ix) const
    {
        assert (ix < this->_nItems);
        return static_cast<diderot::strand_status>(this->_status[ix]);
    }
  // return a pointer to the given strand
    iso_strand *strand (index_t ix) const
    {
        return this->id_to_strand(this->id(ix));
    }
  // return a pointer to the local state of strand ix
    iso_strand *local_state (index_t ix) const
    {
        return this->strand(ix);
    }
  // return a pointer to the local state of strand with the given ID
    iso_strand *id_to_local_state (sid_t id) const
    {
        return this->id_to_strand(id);
    }

  // allocate space for nItems
    bool alloc (uint32_t nItems)
    {
        this->_storage = static_cast<char *>(std::malloc (nItems * sizeof(iso_strand)));
        if (this->_storage == nullptr) {
            return true;
        }
        this->_status = static_cast<uint8_t *>(std::malloc (nItems * sizeof(uint8_t)));
        if (this->_status == nullptr) {
            std::free (this->_storage);
            return true;
        }
        this->_nItems = nItems;
        this->_nActive = 0;
        this->_nStable = 0;
        this->_nFresh = 0;
        return false;
    }

  // initialize the first nStrands locations as new active strands
    void create_strands (uint32_t nStrands)
    {
        assert (this->_nActive == 0);
        assert (this->_nItems == nStrands);
        for (index_t ix = 0;  ix < nStrands;  ix++) {
            this->_status[ix] = diderot::kActive;
            new (this->strand(ix)) iso_strand;
        }
        this->_nActive = nStrands;
        this->_nFresh = nStrands;
    }

  // swap in and out states (NOP for this version)
    void swap () { }

#ifdef DIDEROT_HAS_START_METHOD
  // invoke strand's start method
    diderot::strand_status strand_start (index_t ix)
    {
        return iso_start(this->strand(ix));
    }
#endif // DIDEROT_HAS_START_METHOD

  // invoke strand's update method
    diderot::strand_status strand_update (globals *glob, index_t ix)
    {
        return iso_update(glob, this->strand(ix));
    }

  // invoke strand's stabilize method
    index_t strand_stabilize (index_t ix)
    {
#ifdef DIDEROT_HAS_STABILIZE_METHOD
        iso_stabilize (this->strand(ix));
#endif // DIDEROT_HAS_STABILIZE_METHOD
        this->_status[ix] = diderot::kStable;
        this->_nActive--;
        this->_nStable++;
      // skip to next active strand
	do {
	    ix++;
        } while ((ix < this->_nItems) && (this->_status[ix] != diderot::kActive));
	return ix;
    }

  // mark the given strand as dead
    index_t kill (index_t ix)
    {
        this->_status[ix] = diderot::kDead;
        this->_nActive--;
      // skip to next active strand
	do {
	    ix++;
        } while ((ix < this->_nItems) && (this->_status[ix] != diderot::kActive));
	return ix;
    }

  // finish the local-phase of a superstep (NOP)
    void finish_step () { }

  // finish a kill_all operation (NOP)
    void finish_kill_all () { }

  // finish a stabilize_all operation (NOP)
    void finish_stabilize_all () { }

    index_t begin_alive () const
    {
        index_t ix = 0;
#ifdef DIDEROT_HAS_STRAND_DIE
        while ((ix < this->_nItems) && (this->_status[ix] == diderot::kDead)) {
            ix++;
        }
#endif
        return ix;
    }
    index_t end_alive () const { return this->_nItems; }
    index_t next_alive (index_t &ix) const
    {
        ix++;
#ifdef DIDEROT_HAS_STRAND_DIE
        while ((ix < this->_nItems) && (this->_status[ix] == diderot::kDead)) {
            ix++;
        }
#endif
        return ix;
    }

  // iterator over active strands
    index_t begin_active () const
    {
        index_t ix = 0;
        while ((ix < this->_nItems) && (this->_status[ix] != diderot::kActive)) {
            ix++;
        }
        return ix;
    }
    index_t end_active () const { return this->_nItems; }
    index_t next_active (index_t &ix) const
    {
	do {
	    ix++;
        } while ((ix < this->_nItems) && (this->_status[ix] != diderot::kActive));
        return ix;
    }

  // iterator over stable strands
    index_t begin_stable () const
    {
        index_t ix = 0;
        while ((ix < this->_nItems) && (this->_status[ix] != diderot::kStable)) {
            ix++;
        }
        return ix;
    }
    index_t end_stable () const { return this->_nItems; }
    index_t next_stable (index_t &ix) const
    {
	do {
	    ix++;
        } while ((ix < this->_nItems) && (this->_status[ix] != diderot::kStable));
        return ix;
    }

  // iterator over fresh strands; since the only new strands were created by create_strand
  // we iterate over all of them
    index_t begin_fresh () const { return 0; }
    index_t end_fresh () const { return this->_nFresh; }
    index_t next_fresh (index_t &ix) const { return ++ix; }

}; // struct strand_array

strand_array::~strand_array ()
{
  // run destructors to reclaim any dynamic memory attached to the strand state
    for (auto ix = this->begin_alive();  ix != this->end_alive();  ix = this->next_alive(ix)) {
        this->strand(ix)->~iso_strand();
    }
    if (this->_status != nullptr) std::free (this->_status);
    if (this->_storage != nullptr) std::free (this->_storage);
}
/*---------- end seq-sarr.in ----------*/

struct world : public diderot::world_base {
    strand_array _strands;
    globals *_globals;
    world ();
    ~world ();
    bool init ();
    bool alloc (int32_t base[1], uint32_t size[1]);
    bool create_strands ();
    uint32_t run (uint32_t max_nsteps);
    void swap_state ();
    void kill_all ();
};
// ***** Begin synthesized operations *****

inline float vdot6 (vec6 u, vec6 v)
{
    vec6 w = u * v;
    return w[0] + w[1] + w[2] + w[3] + w[4] + w[5];
}
inline std::array< int, 2 > vtoi2 (vec2 src)
{
    std::array< int, 2 > res = {int32_t(src[0]),int32_t(src[1]),};
    return res;
}
inline float lerp (float a, float b, float t)
{
    return a + t * (b - a);
}
inline vec2 vload2 (const float *vp)
{
    return __extension__ (vec2){vp[0], vp[1]};
}
inline vec2 vcons2 (float r0, float r1)
{
    return __extension__ (vec2){r0, r1};
}
template <typename TY>
inline bool inside2Ds3 (vec2 x0, diderot::image2d< float, TY > img)
{
    return 2 < x0[0] && x0[1] < img.size(1) - 3 && 2 < x0[1] && x0[0] < img.size(0) - 3;
}
inline void vpack2 (tensor_2 &dst, vec2 v0)
{
    dst._data[0] = v0[0];
    dst._data[1] = v0[1];
}
inline vec2 vscale2 (float s, vec2 v)
{
    return __extension__ (vec2){s, s} * v;
}
template <typename TY>
inline tensor_ref_2_2 world2image (diderot::image2d< float, TY > const & img)
{
    return tensor_ref_2_2(img.world2image());
}
inline float vdot2 (vec2 u, vec2 v)
{
    vec2 w = u * v;
    return w[0] + w[1];
}
template <typename TY>
inline tensor_ref_2 translate (diderot::image2d< float, TY > const & img)
{
    return tensor_ref_2(img.translate());
}
inline vec6 vcons6 (float r0, float r1, float r2, float r3, float r4, float r5)
{
    return __extension__ (vec6){r0, r1, r2, r3, r4, r5, 0.0f, 0.0f};
}
inline vec2 vfloor2 (vec2 v)
{
    return __extension__ (vec2){std::floor(v[0]), std::floor(v[1])};
}
// ***** End synthesized operations *****

typedef struct {
    float gv_isoval;
    int32_t gv_stepsMax;
    float gv_epsilon;
    std::string gv_img;
    tensor_2 gv_cmin;
    tensor_2 gv_cmax;
    int32_t gv_size;
} cmd_line_inputs;
static void init_defaults (cmd_line_inputs *inp)
{
    inp->gv_img = "../symb/a.nrrd";
    inp->gv_isoval = 0.4e0f;
    inp->gv_stepsMax = 10;
    inp->gv_epsilon = 0.1e-2f;
    inp->gv_cmin[0] = -0.1e1f;
    inp->gv_cmin[1] = -0.1e1f;
    inp->gv_cmax[0] = 0.1e1f;
    inp->gv_cmax[1] = 0.1e1f;
    inp->gv_size = 30;
}
static void register_inputs (cmd_line_inputs *inp, diderot::options< float, int32_t > *opts)
{
    opts->add("isoval", "isovalue of isosurface to sample", &inp->gv_isoval, true);
    opts->add("stepsMax", "max # steps allowed for convergence", &inp->gv_stepsMax, true);
    opts->add("epsilon", "convergence threshold", &inp->gv_epsilon, true);
    opts->add("img", "data to isocontour", &inp->gv_img, true);
    opts->add("cmin", "# lower corner of sampling grid", 2, inp->gv_cmin._data, true);
    opts->add("cmax", "# upper corner of sampling grid", 2, inp->gv_cmax._data, true);
    opts->add("size", "# samples on both axes of sampling grid", &inp->gv_size, true);
}
static bool init_inputs (world *wrld, cmd_line_inputs *inp)
{
    globals *glob = wrld->_globals;
    glob->gv_isoval = inp->gv_isoval;
    glob->gv_stepsMax = inp->gv_stepsMax;
    glob->gv_epsilon = inp->gv_epsilon;
    if (glob->gv_img.load(wrld, inp->gv_img)) {
        return true;
    }
    glob->gv_cmin = inp->gv_cmin;
    glob->gv_cmax = inp->gv_cmax;
    glob->gv_size = inp->gv_size;
    return false;
}
static std::string Outfile = "pos";
static void register_outputs (diderot::options< float, int32_t > *opts)
{
    opts->add("o,output", "specify output-file file", &Outfile, true);
}
static bool init_globals (world *wrld)
{
    globals *glob = wrld->_globals;
    return false;
}
static void iso_init (iso_strand *self, int32_t p_ID_2, tensor_ref_2 p_pos0_3)
{
    self->sv_pos = p_pos0_3;
    self->sv_steps = 0;
}
static diderot::strand_status iso_update (globals *glob, iso_strand *self)
{
    bool l__t_7;
    tensor_ref_2_2 l_Mtransform_4 = world2image(glob->gv_img);
    vec2 v_5 = vcons2(vdot2(vload2(l_Mtransform_4.last(0).addr(0)), vload2(tensor_ref_2(self->sv_pos).addr(0))),
        vdot2(vload2(l_Mtransform_4.last(2).addr(0)), vload2(tensor_ref_2(self->sv_pos).addr(0)))) + vload2(
        translate(glob->gv_img).addr(0));
    vec2 v_6 = v_5;
    if (!inside2Ds3(v_5, glob->gv_img)) {
        l__t_7 = true;
    }
    else {
        l__t_7 = self->sv_steps > glob->gv_stepsMax;
    }
    if (l__t_7) {
        return diderot::kDie;
    }
    vec2 v_8 = vfloor2(v_6);
    vec2 v_9 = v_6 - v_8;
    std::array< int32_t, 2 > l_n_10 = vtoi2(v_8);
    int32_t l_idx_11 = l_n_10[0] + -2;
    int32_t l_idx_12 = l_n_10[1] + -2;
    int32_t l_mulRes_13 = 101 * l_idx_12;
    int32_t l_addRes_14 = l_idx_11 + 1;
    int32_t l_addRes_15 = l_idx_11 + 2;
    int32_t l_addRes_16 = l_idx_11 + 3;
    int32_t l_addRes_17 = l_idx_11 + 4;
    int32_t l_addRes_18 = l_idx_11 + 5;
    vec6 v_19 = vcons6(glob->gv_img[l_idx_11 + l_mulRes_13], glob->gv_img[l_addRes_14 + l_mulRes_13],
        glob->gv_img[l_addRes_15 + l_mulRes_13], glob->gv_img[l_addRes_16 + l_mulRes_13],
        glob->gv_img[l_addRes_17 + l_mulRes_13], glob->gv_img[l_addRes_18 + l_mulRes_13]);
    int32_t l_mulRes_20 = 101 * (l_idx_12 + 1);
    vec6 v_21 = vcons6(glob->gv_img[l_idx_11 + l_mulRes_20], glob->gv_img[l_addRes_14 + l_mulRes_20],
        glob->gv_img[l_addRes_15 + l_mulRes_20], glob->gv_img[l_addRes_16 + l_mulRes_20],
        glob->gv_img[l_addRes_17 + l_mulRes_20], glob->gv_img[l_addRes_18 + l_mulRes_20]);
    int32_t l_mulRes_22 = 101 * (l_idx_12 + 2);
    vec6 v_23 = vcons6(glob->gv_img[l_idx_11 + l_mulRes_22], glob->gv_img[l_addRes_14 + l_mulRes_22],
        glob->gv_img[l_addRes_15 + l_mulRes_22], glob->gv_img[l_addRes_16 + l_mulRes_22],
        glob->gv_img[l_addRes_17 + l_mulRes_22], glob->gv_img[l_addRes_18 + l_mulRes_22]);
    int32_t l_mulRes_24 = 101 * (l_idx_12 + 3);
    vec6 v_25 = vcons6(glob->gv_img[l_idx_11 + l_mulRes_24], glob->gv_img[l_addRes_14 + l_mulRes_24],
        glob->gv_img[l_addRes_15 + l_mulRes_24], glob->gv_img[l_addRes_16 + l_mulRes_24],
        glob->gv_img[l_addRes_17 + l_mulRes_24], glob->gv_img[l_addRes_18 + l_mulRes_24]);
    int32_t l_mulRes_26 = 101 * (l_idx_12 + 4);
    vec6 v_27 = vcons6(glob->gv_img[l_idx_11 + l_mulRes_26], glob->gv_img[l_addRes_14 + l_mulRes_26],
        glob->gv_img[l_addRes_15 + l_mulRes_26], glob->gv_img[l_addRes_16 + l_mulRes_26],
        glob->gv_img[l_addRes_17 + l_mulRes_26], glob->gv_img[l_addRes_18 + l_mulRes_26]);
    int32_t l_mulRes_28 = 101 * (l_idx_12 + 5);
    vec6 v_29 = vcons6(glob->gv_img[l_idx_11 + l_mulRes_28], glob->gv_img[l_addRes_14 + l_mulRes_28],
        glob->gv_img[l_addRes_15 + l_mulRes_28], glob->gv_img[l_addRes_16 + l_mulRes_28],
        glob->gv_img[l_addRes_17 + l_mulRes_28], glob->gv_img[l_addRes_18 + l_mulRes_28]);
    float l_vY__30 = v_9[1];
    vec6 v_31 = vcons6(l_vY__30 + 0.2e1f, l_vY__30 + 0.1e1f, l_vY__30, l_vY__30 - 0.1e1f, l_vY__30 - 0.2e1f,
        l_vY__30 - 0.3e1f);
    vec6 v_32 = vcons6(0.961875e1f, 0.1875e-1f, 0.8625e0f, 0.8625e0f, 0.1875e-1f, 0.961875e1f);
    vec6 v_33 = vcons6(-0.23625e2f, 0.4375e1f, 0.0f, 0.0f, -0.4375e1f, 0.23625e2f);
    vec6 v_34 = vcons6(0.2334375e2f, -0.1065625e2f, -0.14375e1f, -0.14375e1f, -0.1065625e2f, 0.2334375e2f);
    vec6 v_35 = vcons6(-0.12e2f, 0.10e2f, 0.0f, 0.0f, -0.10e2f, 0.12e2f);
    vec6 v_36 = vcons6(0.340625e1f, -0.459375e1f, 0.11875e1f, 0.11875e1f, -0.459375e1f, 0.340625e1f);
    vec6 v_37 = vcons6(-0.508333333333e0f, 0.104166666667e1f, -0.583333333333e0f, 0.583333333333e0f,
        -0.104166666667e1f, 0.508333333333e0f);
    vec6 v_38 = vcons6(0.3125e-1f, -0.9375e-1f, 0.625e-1f, 0.625e-1f, -0.9375e-1f, 0.3125e-1f);
    vec6 v_39 = v_32 + v_31 * (v_33 + v_31 * (v_34 + v_31 * (v_35 + v_31 * (v_36 + v_31 * (v_37 + v_31 * v_38)))));
    vec6 v_40 = vcons6(0.466875e2f, -0.213125e2f, -0.2875e1f, -0.2875e1f, -0.213125e2f, 0.466875e2f);
    vec6 v_41 = vcons6(-0.36e2f, 0.30e2f, 0.0f, 0.0f, -0.30e2f, 0.36e2f);
    vec6 v_42 = vcons6(0.13625e2f, -0.18375e2f, 0.475e1f, 0.475e1f, -0.18375e2f, 0.13625e2f);
    vec6 v_43 = vcons6(-0.254166666667e1f, 0.520833333333e1f, -0.291666666667e1f, 0.291666666667e1f,
        -0.520833333333e1f, 0.254166666667e1f);
    vec6 v_44 = vcons6(0.1875e0f, -0.5625e0f, 0.375e0f, 0.375e0f, -0.5625e0f, 0.1875e0f);
    float l_vX__45 = v_9[0];
    vec6 v_46 = vcons6(l_vX__45 + 0.2e1f, l_vX__45 + 0.1e1f, l_vX__45, l_vX__45 - 0.1e1f, l_vX__45 - 0.2e1f,
        l_vX__45 - 0.3e1f);
    vec6 v_47 = v_32 + v_46 * (v_33 + v_46 * (v_34 + v_46 * (v_35 + v_46 * (v_36 + v_46 * (v_37 + v_46 * v_38)))));
    vec6 v_48 = v_33 + v_46 * (v_40 + v_46 * (v_41 + v_46 * (v_42 + v_46 * (v_43 + v_46 * v_44))));
    vec6 v_49 = vcons6(vdot6(v_47, v_19), vdot6(v_47, v_21), vdot6(v_47, v_23), vdot6(v_47, v_25), vdot6(v_47, v_27),
        vdot6(v_47, v_29));
    vec2 v_50 = vcons2(
        vdot6(v_39,
            vcons6(vdot6(v_48, v_19), vdot6(v_48, v_21), vdot6(v_48, v_23), vdot6(v_48, v_25), vdot6(v_48, v_27),
                vdot6(v_48, v_29))),
        vdot6(v_33 + v_31 * (v_40 + v_31 * (v_41 + v_31 * (v_42 + v_31 * (v_43 + v_31 * v_44)))), v_49));
    vec2 v_51 = vcons2(vdot2(v_50, vcons2(l_Mtransform_4[0], l_Mtransform_4[2])),
        vdot2(v_50, vcons2(l_Mtransform_4[1], l_Mtransform_4[3])));
    float l__t_52 = std::sqrt(vdot2(v_51, v_51));
    vec6 v_53 = v_49;
    vec6 v_54 = v_39;
    vec2 v_55 = v_51;
    if (l__t_52 == 0.0f) {
        return diderot::kDie;
    }
    float l_op1_e3_l_23_56 = 0.1e1f / l__t_52;
    vec2 v_57 = vscale2(vdot6(v_54, v_53) - glob->gv_isoval, -vscale2(l_op1_e3_l_23_56, v_55));
    vec2 v_58 = vcons2(l_op1_e3_l_23_56 * v_57[0], l_op1_e3_l_23_56 * v_57[1]);
    vec2 v_59 = vload2(tensor_ref_2(self->sv_pos).addr(0)) + v_58;
    vec2 v_60 = v_59;
    if (std::sqrt(vdot2(v_58, v_58)) < glob->gv_epsilon) {
        vpack2(self->sv_pos, v_60);
        return diderot::kStabilize;
    }
    vpack2(self->sv_pos, v_60);
    self->sv_steps = self->sv_steps + 1;
    return diderot::kActive;
}
bool output_get_pos (world *wrld, Nrrd *nData)
{
    // Compute sizes of nrrd file
    size_t sizes[2];
    sizes[0] = 2;
    sizes[1] = wrld->_strands.num_stable();
    // check for empty output
    if (0 == wrld->_strands.num_stable()) {
        wrld->error("no stable strands at termination, so no output");
        nrrdEmpty(nData);
        return true;
    }
    // Allocate nData nrrd
    if (nrrdMaybeAlloc_nva(nData, nrrdTypeFloat, 2, sizes) != 0) {
        char *msg = biffGetDone(NRRD);
        biffMsgAdd(wrld->_errors, msg);
        std::free(msg);
        return true;
    }
    // copy data to output nrrd
    char *cp = reinterpret_cast<char *>(nData->data);
    for (auto ix = wrld->_strands.begin_stable(); ix != wrld->_strands.end_stable(); ix = wrld->_strands.next_stable(
        ix)) {
        memcpy(cp, &wrld->_strands.strand(ix)->sv_pos, 2 * sizeof(float));
        cp += 2 * sizeof(float);
    }
    nData->axis[0].kind = nrrdKind2Vector;
    nData->axis[1].kind = nrrdKindList;
    return false;
}
static void write_output (world *wrld)
{
    Nrrd *nData;
    nData = nrrdNew();
    if (output_get_pos(wrld, nData)) {
        std::cerr << "Error getting nrrd data:\n" << biffMsgStrGet(wrld->_errors) << std::endl;
        exit(1);
    }
    else if (nrrd_save_helper(Outfile, "", "nrrd", nData)) {
        exit(1);
    }
    nrrdNuke(nData);
}
/*---------- begin world-methods.in ----------*/
// Allocate the program's world
//
world::world ()
    : diderot::world_base (ProgramName, false, 1)
{
#ifndef DIDEROT_NO_GLOBALS
    this->_globals = new globals;
#endif

#ifdef DIDEROT_HAS_STRAND_COMMUNICATION
    this->_tree = nullptr;
#endif
} // world constructor

// shutdown and deallocate the world
//
world::~world ()
{
#ifndef DIDEROT_NO_GLOBALS
    delete this->_globals;
#endif

#ifdef DIDEROT_HAS_STRAND_COMMUNICATION
    delete this->_tree;
#endif

} // world destructor

// Initialize the program's world
//
bool world::init ()
{
    if (this->_stage != diderot::POST_NEW) {
        biffMsgAdd (this->_errors, "multiple calls to world::init");
        return true;
    }

#if !defined(DIDEROT_STANDALONE_EXEC) && !defined(DIDEROT_NO_INPUTS)
  // initialize the defined flags for the input globals
    init_defined_inputs (this);
#endif

    this->_stage = diderot::POST_INIT;

    return false;

}

// allocate the initial strands and initialize the rest of the world structure.
//
bool world::alloc (int32_t base[1], uint32_t size[1])
{
    size_t numStrands = 1;
    for (uint32_t i = 0;  i < 1;  i++) {
        numStrands *= size[i];
        this->_base[i] = base[i];
        this->_size[i] = size[i];
    }

    if (this->_verbose) {
        std::cerr << "world::alloc: " << size[0];
        for (uint32_t i = 1;  i < 1;  i++) {
            std::cerr << " x " << size[i];
        }
        std::cerr << std::endl;
    }

#ifdef DIDEROT_TARGET_PARALLEL
  // determine the block size based on the initial number of strands and the
  // number of workers
    this->_strands.set_block_size (this->_sched->_numWorkers, numStrands);
#endif

  // allocate the strand array
    if (this->_strands.alloc (numStrands)) {
        biffMsgAdd (this->_errors, "unable to allocate strand-state array\n");
        return true;
    }

  // initialize strand state pointers etc.
    this->_strands.create_strands (numStrands);

#ifdef DIDEROT_HAS_STRAND_COMMUNICATION
    this->_tree = new diderot::kdtree<0, float, strand_array> (&this->_strands);
#endif

    return false;

} // world::alloc

// swap input and output states
//
inline void world::swap_state ()
{
    this->_strands.swap ();
}

#ifdef DIDEROT_HAS_KILL_ALL
void world::kill_all ()
{
    if (this->_strands.num_active() > 0) {
        for (auto ix = this->_strands.begin_active();
            ix != this->_strands.end_active();
            )
        {
            assert (this->_strands.status(ix) == diderot::kActive);
            ix = this->_strands.kill (ix);
        }
        this->_strands.finish_kill_all();
    }
    assert (this->_strands.num_active() == 0);
}
#endif

#ifdef DIDEROT_HAS_STABILIZE_ALL
void world::stabilize_all ()
{
#ifndef DIDEROT_NO_GLOBALS
    globals *glob = this->_globals;
#endif

    if (this->_strands.num_active() > 0) {
        for (auto ix = this->_strands.begin_active();
            ix != this->_strands.end_active();
            )
        {
            assert (this->_strands.status(ix) == diderot::kActive);
	    this->_strands._status[ix] = diderot::kStable;
            ix = this->_strands.strand_stabilize (ix);
        }
        this->_strands.finish_stabilize_all();
    }
    assert (this->_strands.num_active() == 0);
}
#endif
/*---------- end world-methods.in ----------*/

bool world::create_strands ()
{
    if (init_globals(this)) {
        return true;
    }
    globals *glob = this->_globals;
    int32_t l__t_63 = glob->gv_size - 1;
    int lo_0 = 0;
    int lo_1 = 0;
    int32_t base[1] = {0,};
    uint32_t size[1] = {static_cast<uint32_t>((l__t_63 - lo_0 + 1) * (l__t_63 - lo_1 + 1)),};
    if (this->alloc(base, size)) {
        return true;
    }
    uint32_t ix = 0;
    for (int i_idx1_64 = lo_0; i_idx1_64 <= l__t_63; i_idx1_64++) {
        for (int i_idx0_65 = lo_1; i_idx0_65 <= l__t_63; i_idx0_65++) {
            float l_op1_e3_l_5_66 = static_cast<float>(l__t_63) - 0.0f;
            tensor_2 _arg_67 = {lerp(tensor_ref_2(glob->gv_cmin)[0], tensor_ref_2(glob->gv_cmax)[0],
                    (static_cast<float>(i_idx0_65) - 0.0f) / l_op1_e3_l_5_66),lerp(tensor_ref_2(glob->gv_cmin)[1],
                    tensor_ref_2(glob->gv_cmax)[1], (static_cast<float>(i_idx1_64) - 0.0f) / l_op1_e3_l_5_66),};
            iso_init(this->_strands.strand(ix), i_idx0_65 + glob->gv_size * i_idx1_64, _arg_67);
            ++ix;
        }
    }
    this->swap_state();
    this->_stage = diderot::POST_CREATE;
    return false;
}
/*---------- begin seq-run-nobsp.in ----------*/
//! Run the Diderot program (sequential version without BSP semantics)
//! \param max_nsteps the limit on the number of super steps; 0 means unlimited
//! \return the number of steps taken, or 0 on error.
uint32_t world::run (uint32_t max_nsteps)
{
    if (this->_stage < diderot::POST_CREATE) {
        biffMsgAdd (this->_errors, "attempt to run uninitialized program\n");
        return 0;
    }
    else if (this->_stage == diderot::DONE) {
        return 0;
    }
    else if (this->_stage == diderot::POST_CREATE) {
#ifdef DIDEROT_HAS_GLOBAL_START
        this->global_start();
#endif
        this->_stage = diderot::RUNNING;
    }
    assert (this->_stage == diderot::RUNNING);

#ifndef DIDEROT_NO_GLOBALS
    globals *glob = this->_globals;
#endif

    if (max_nsteps == 0) {
        max_nsteps = 0xffffffff;  // essentially unlimited
    }

    double t0 = airTime();

    if (this->_verbose) {
        std::cerr << "run with " << this->_strands.num_alive() << " strands ..." << std::endl;
    }

#ifdef DIDEROT_HAS_START_METHOD
    this->run_start_methods();
#endif

  // iterate until all strands are stable
    uint32_t maxSteps = 0;
    for (auto ix = this->_strands.begin_active();
         ix != this->_strands.end_active();
         )
    {
        diderot::strand_status sts = this->_strands.status(ix);
        uint32_t nSteps = 0;
        while ((! sts) && (nSteps < max_nsteps)) {
            nSteps++;
            sts = this->_strands.strand_update(glob, ix);
        }
        switch (sts) {
          case diderot::kStabilize:
          // stabilize the strand's state.
            ix = this->_strands.strand_stabilize (ix);
            break;
#ifdef DIDEROT_HAS_STRAND_DIE
          case diderot::kDie:
            ix = this->_strands.kill (ix);
            break;
#endif
          default:
            assert (sts == this->_strands.status(ix));
	    ix = this->_strands.next_active(ix);
            break;
        }
        if (maxSteps < nSteps) maxSteps = nSteps;
    }

    this->_run_time += airTime() - t0;

    if (this->_strands.num_active() == 0)
        this->_stage = diderot::DONE;

    return maxSteps;

} // world::run
/*---------- end seq-run-nobsp.in ----------*/

/*---------- begin namespace-close.in ----------*/

} // namespace Diderot
/*---------- end namespace-close.in ----------*/

/*---------- begin seq-main.in ----------*/
using namespace Diderot;

//! Main function for standalone sequential C target
//
int main (int argc, const char **argv)
{
    bool        timingFlg = false;      //! true if timing computation
    uint32_t    stepLimit = 0;          //! limit on number of execution steps (0 means unlimited)
    std::string printFile = "-";        //! file to direct printed output into
#ifdef DIDEROT_EXEC_SNAPSHOT
    uint32_t    snapshotPeriod = 0;     //! supersteps per snapshot; 0 means no snapshots
#endif
    uint32_t    nSteps = 0;             //! number of supersteps taken

  // create the world
    world *wrld = new (std::nothrow) world();
    if (wrld == nullptr) {
        std::cerr << "unable to create world" << std::endl;
        exit (1);
    }

#ifndef DIDEROT_NO_INPUTS
  // initialize the default values for the inputs
    cmd_line_inputs inputs;
    init_defaults (&inputs);
#endif

  // handle command-line options
    {
        diderot::options<float,int32_t> *opts = new diderot::options<float,int32_t> ();
        opts->add ("l,limit", "specify limit on number of super-steps (0 means unlimited)",
            &stepLimit, true);
#ifdef DIDEROT_EXEC_SNAPSHOT
        opts->add ("s,snapshot",
            "specify number of super-steps per snapshot (0 means no snapshots)",
            &snapshotPeriod, true);
#endif
        opts->add ("print", "specify where to direct printed output", &printFile, true);
        opts->addFlag ("v,verbose", "enable runtime-system messages", &(wrld->_verbose));
        opts->addFlag ("t,timing", "enable execution timing", &timingFlg);
#ifndef DIDEROT_NO_INPUTS
      // register options for setting global inputs
        register_inputs (&inputs, opts);
#endif
        register_outputs (opts);
        opts->process (argc, argv);
        delete opts;
    }

  // redirect printing (if necessary)
    if (printFile.compare("-") != 0) {
        wrld->_printTo = new std::ofstream (printFile);
        if (wrld->_printTo->fail()) {
            std::cerr << "Error opening print file" << std::endl;
            exit(1);
        }
    }

  // initialize scheduler stuff
    if (wrld->_verbose) {
        std::cerr << "initializing world ..." << std::endl;
    }
    if (wrld->init()) {
        std::cerr << "Error initializing world:\n" << wrld->get_errors() << std::endl;
        exit(1);
    }

#ifndef DIDEROT_NO_INPUTS
  // initialize the input globals
    if (init_inputs (wrld, &inputs)) {
        std::cerr << "Error initializing inputs:\n" << wrld->get_errors() << std::endl;
        exit(1);
    }
#endif

  // run the generated global initialization code
    if (wrld->_verbose) {
        std::cerr << "initializing globals and creating strands ...\n";
    }
    if (wrld->create_strands()) {
        std::cerr << "Error in global initialization:\n"
            << wrld->get_errors() << std::endl;
        exit(1);
    }

#ifdef DIDEROT_EXEC_SNAPSHOT

    if (snapshotPeriod > 0) {
     // write initial state as snapshot 0
        write_snapshot (wrld, "-0000");
     // run the program for `snapshotPeriod` steps at a time with a snapshot after each run
        while (true) {
            uint32_t n, limit;
          // determine a step limit for the next run
            if (stepLimit > 0) {
                if (stepLimit <= nSteps) {
                    break;
                }
                limit = std::min(stepLimit - nSteps, snapshotPeriod);
            }
            else {
                limit = snapshotPeriod;
            }
          // run the program for upto limit steps
            if ((n = wrld->run (limit)) == 0) {
                break;
            }
            nSteps += n;
            if ((wrld->_errors->errNum > 0) || (wrld->_strands.num_alive() == 0)) {
                break;
            }
          // write a snapshot with the step count as a suffix
            std::string suffix = std::to_string(nSteps);
            if (suffix.length() < 4) {
                suffix = std::string("0000").substr(0, 4 - suffix.length()) + suffix;
            }
            suffix = "-" + suffix;
            write_snapshot (wrld, suffix);
        }
    }
    else {
        nSteps = wrld->run (stepLimit);
    }

#else // !DIDEROT_EXEC_SNAPSHOT

    nSteps = wrld->run (stepLimit);

#endif // DIDEROT_EXEC_SNAPSHOT

    if (wrld->_errors->errNum > 0) {
        std::cerr << "Error during execution:\n" << wrld->get_errors() << std::endl;
        exit(1);
    }

    if ((stepLimit != 0) && (wrld->_strands.num_active() > 0)) {
#ifdef DIDEROT_STRAND_ARRAY
        if (wrld->_verbose) {
            std::cerr << "Step limit expired; "
                << wrld->_strands.num_active() << " active strands remaining" << std::endl;
        }
#else
      // step limit expired, so kill remaining strands
        if (wrld->_verbose) {
            std::cerr << "Step limit expired. Killing remaining "
                << wrld->_strands.num_active() << " active strands" << std::endl;
        }
        wrld->kill_all();
#endif
    }

    if (wrld->_verbose) {
        std::cerr << "done: " << nSteps << " steps, in " << wrld->_run_time << " seconds"
            << std::endl;
    }
    else if (timingFlg) {
        std::cout << "usr=" << wrld->_run_time << std::endl;
    }

  // output the final strand states
    write_output (wrld);

    delete wrld;

    return 0;

} // main
/*---------- end seq-main.in ----------*/

